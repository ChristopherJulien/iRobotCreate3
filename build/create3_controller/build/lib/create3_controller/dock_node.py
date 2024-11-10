# create3_controller/dock_node.py

import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class DockNode(Node):
    def __init__(self):
        super().__init__('dock_node')
        self.cli = self.create_client(Empty, '/dock')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for dock service...')

        self.req = Empty.Request()

    def send_request(self):
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    dock_node = DockNode()
    dock_node.send_request()

    while rclpy.ok():
        rclpy.spin_once(dock_node)
        if dock_node.future.done():
            try:
                dock_node.future.result()
            except Exception as e:
                dock_node.get_logger().error(f'Service call failed: {e}')
            else:
                dock_node.get_logger().info('Docked successfully')
            break

    dock_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
