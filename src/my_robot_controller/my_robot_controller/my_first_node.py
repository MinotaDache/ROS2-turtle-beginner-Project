#!/usr/bin/env python3

import rclpy # Import the rclpy library
from rclpy.node import Node # Import the Node class

class MyNode(Node): # create a class that inherits from the Node class
    def __init__(self):
        super().__init__("first_node") # we initialized the node
        self.counter_ = 0 # initialize a counter
        self.create_timer(1.0,self.timer_callback)

    
    def timer_callback(self): 
        self.get_logger().info("Hello ROS2 " + str(self.counter_))
        self.counter_ += 1 # increment the counter


def main(args=None):
    rclpy.init(args=args) # Initialize ros2 communication
    node = MyNode()
    rclpy.spin(node) # keep the node running until it is shutdown

    rclpy.shutdown() # Shutdown the ros2 communication

if __name__ == '__main__': # useful if we want to directly run this file from the terminal
    main() # Call the main function


