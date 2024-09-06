#!/usr/bin/env python3

import random
import time
import rclpy
from rclpy.node import Node

class SensorData:
    def __init__(self, temperature, pressure, humidity):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity 

    def __str__(self):
        return (f"Temperature: {self.temperature:.2f}°C, "
                f"Pressure: {self.pressure:.2f} hPa, "
                f"Humidity: {self.humidity:.2f}%")

class DataCollectorNode(Node):
    def __init__(self, temperature_range, pressure_range, humidity_range):
        super().__init__('data_collector_node')
        self.temperature_range = temperature_range
        self.pressure_range = pressure_range
        self.humidity_range = humidity_range
        self.timer = self.create_timer(1.0, self.timer_callback)

    def generate_random_data(self):
        temperature = random.uniform(*self.temperature_range)
        pressure = random.uniform(*self.pressure_range)
        humidity = random.uniform(*self.humidity_range)
        return SensorData(temperature, pressure, humidity)

    def timer_callback(self):
        data = self.generate_random_data()
        self.get_logger().info(str(data))

def main(args=None):
    rclpy.init(args=args)
    temperature_range = (15.0, 30.0)
    pressure_range = (950.0, 1050.0)
    humidity_range = (30.0, 70.0)
    node = DataCollectorNode(temperature_range, pressure_range, humidity_range)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
