#!/usr/bin/env python3 # its interpreter
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # Import the Twist message type

class DrawCircleNode(Node):

    def __init__(self): # Constructor
        super().__init__("draw_circle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) # create a publisher to publish velocity commands
        self.timer_ = self.create_timer(0.5, self.send_velocity_cmd)
        self.get_logger().info("Draw Circle Node has been started")
    
    def send_velocity_cmd(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg) # publish the message


    

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode() # create an instance of the DrawCircleNode class

    rclpy.spin(node)
    rclpy.shutdown()

