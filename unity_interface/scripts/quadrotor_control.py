#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
import math

class CameraController(Node):
    def __init__(self):
        super().__init__('camera_controller')
        self.pub = self.create_publisher(Pose, '/quadrotor/pose_cmd', 10)
        timer_period = 0.1  # seconds (10 Hz)
        self.create_timer(timer_period, self.publish_pose)
        self.angle = 0.0
        self.pose = Pose()
        self.pose.position.z = 20.0

    def publish_pose(self):
        # rotate around z-axis
        self.angle += 0.02
        self.pose.orientation.z = math.sin(self.angle / 2.0)
        self.pose.orientation.w = math.cos(self.angle / 2.0)
        # position to x, y, z
        self.pose.position.x = 0.0
        self.pose.position.y = 0.0
        self.pub.publish(self.pose)
        self.get_logger().info(f'Published quadrotor pose: {self.pose.position.x:.2f}, {self.pose.position.y:.2f}, {self.pose.position.z:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = CameraController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()