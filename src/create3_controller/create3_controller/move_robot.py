# create3_controller/move_robot.py

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
import yaml
import math
from ament_index_python.packages import get_package_share_directory

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10)
        self.position = None
        self.yaw = None
        self.x_goal = None
        self.y_goal = None
        self.theta_goal = None
        self.waypoints = []
        self.index = 0
        self.goal_read = False
        self.declare_parameter('goal_file', '')
        self.declare_parameter('path_type', '')
        self.timer = self.create_timer(0.1, self.timer_callback)

    def listener_callback(self, msg):
        self.position = msg.pose.pose.position
        orientation_q = msg.pose.pose.orientation
        _, _, self.yaw = euler_from_quaternion([
            orientation_q.x,
            orientation_q.y,
            orientation_q.z,
            orientation_q.w
        ])

    def timer_callback(self):
        if self.position is None or self.yaw is None:
            return
        if not self.goal_read:
            self.read_goal()
            self.compute_waypoints()
            self.goal_read = True
        self.move_towards_waypoint()

    def read_goal(self):
        try:
            goal_file = self.get_parameter('goal_file').get_parameter_value().string_value

            if not goal_file:
                package_share_directory = get_package_share_directory('create3_controller')
                goal_file = package_share_directory + '/config/goal.yaml'

            with open(goal_file, 'r') as file:
                data = yaml.safe_load(file)
                goal = data['goal_position']
            
            self.x_goal = goal['x']
            self.y_goal = goal['y']
            self.theta_goal = goal['theta']
        
        except Exception as e:
            self.get_logger().error(f'Failed to read goal file: {e}')
            rclpy.shutdown()

    def compute_waypoints(self):
        pattern = [
            {'x': 0.0, 'y': 0.0},
            {'x': 0.4615, 'y': 0.0},
            {'x': 0.6923, 'y': 0.2154},
            {'x': 0.6923, 'y': 0.6923},
            {'x': -0.3077, 'y': 0.6923},
            {'x': 0.0256, 'y': 1.0},
            {'x': 1.0, 'y': 1.0},
            {'x': 0.6923, 'y': 0.6923},
            {'x': 0.0, 'y': 0.0},
        ]
        self.waypoints = [
            {'x': p['x'] * self.x_goal, 'y': p['y'] * self.y_goal} for p in pattern
        ]

    def move_towards_waypoint(self):
        if self.index >= len(self.waypoints):
            self.get_logger().info('All waypoints reached')
            self.publisher_.publish(Twist())  # Stop the robot
            return

        target_x = self.waypoints[self.index]['x']
        target_y = self.waypoints[self.index]['y']

        # Compute distance to the goal
        distance = math.hypot(target_x - self.position.x, target_y - self.position.y)

        # If we are close enough to the waypoint, move to the next one
        if distance < 0.1:
            self.get_logger().info(f'Waypoint {self.index} reached')
            self.index += 1
            return

        # Compute the angle to the goal
        angle_to_goal = math.atan2(target_y - self.position.y, target_x - self.position.x)

        # Compute the difference between the current yaw and the angle to the goal
        angle_diff = self.normalize_angle(angle_to_goal - self.yaw)

        # Create a Twist message to send velocities
        cmd = Twist()

        # Determine movement based on angle difference
        if abs(angle_diff) > 0.1:
            # Rotate towards the goal
            cmd.linear.x = 0.0
            cmd.angular.z = 1.0 * angle_diff
        else:
            # Move forward towards the goal
            cmd.linear.x = 0.2  # Constant forward speed
            cmd.angular.z = 0.0

        self.publisher_.publish(cmd)

    @staticmethod
    def normalize_angle(angle):
        """Normalize the angle to be within [-pi, pi]."""
        while angle > math.pi:
            angle -= 2 * math.pi
        while angle < -math.pi:
            angle += 2 * math.pi
        return angle

def main(args=None):
    rclpy.init(args=args)
    move_robot = MoveRobot()
    rclpy.spin(move_robot)
    move_robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
