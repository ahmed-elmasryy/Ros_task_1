#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import time

class NumCheckNode(Node):
    def __init__(self, number):
        super().__init__('num_check_node')
        self.number = number
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info(f"Checking if {self.number} is even or odd...")

    def is_even(self):
        return self.number % 2 == 0

    def timer_callback(self):
        if self.is_even():
            self.get_logger().info(f"{self.number} is even.")
        else:
            self.get_logger().info(f"{self.number} is odd.")

def main(args=None):
    rclpy.init(args=args)
    number = int(input("Enter a number: "))
    num_check_node = NumCheckNode(number)
    rclpy.spin(num_check_node)
    num_check_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
