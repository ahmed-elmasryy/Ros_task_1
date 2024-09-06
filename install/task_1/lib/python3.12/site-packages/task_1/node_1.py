# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time

class Num_check:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        return self.number % 2 == 0

    def print_result(self):
        if self.is_even():
            print(f"{self.number} is even.")
        else:
            print(f"{self.number} is odd.")

    def start_checking(self):
        while True:
            self.print_result()
            time.sleep(1)  


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    checker = Num_check(number)
    checker.start_checking()
