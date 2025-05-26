#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TwistSubscriber(Node):
    def __init__(self):
        super().__init__('twist_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            '/my_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: linear.x={msg.linear.x}, angular.z={msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = TwistSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
