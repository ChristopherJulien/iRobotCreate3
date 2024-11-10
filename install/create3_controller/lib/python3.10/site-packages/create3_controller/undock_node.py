# create3_controller/undock_node.py

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from irobot_create_msgs.action import Undock

class UndockClient(Node):

    def __init__(self):
        super().__init__('undock_client')
        self._action_client = ActionClient(self, Undock, '/undock')

    def send_goal(self):
        goal_msg = Undock.Goal()

        self.get_logger().info('Waiting for undock action server...')
        self._action_client.wait_for_server()

        self.get_logger().info('Sending undock goal...')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Undock goal rejected')
            return

        self.get_logger().info('Undock goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Undock Feedback: {feedback}')

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Undock action completed')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    undock_client = UndockClient()
    undock_client.send_goal()
    rclpy.spin(undock_client)

if __name__ == '__main__':
    main()
