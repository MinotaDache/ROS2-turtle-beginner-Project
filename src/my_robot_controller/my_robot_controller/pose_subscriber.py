#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber_ = self.create_subscription(  # ✅ Fixed variable name
            Pose, "turtle1/pose", self.pose_callback, 10
        )
        self.get_logger().info("Pose Subscriber Node has been started!")  # ✅ Logging for confirmation

    def pose_callback(self, msg: Pose):
        self.get_logger().info(f"Received Pose: x={msg.x}, y={msg.y}, theta={msg.theta}")  # ✅ Better logging


def main(args= None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()