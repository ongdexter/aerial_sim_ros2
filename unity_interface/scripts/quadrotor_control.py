#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
import math

class CameraController(Node):
    def __init__(self):
        super().__init__('camera_controller')
        self.pub = self.create_publisher(Pose, '/camera/pose_cmd', 10)
        timer_period = 0.1  # seconds (10 Hz)
        self.create_timer(timer_period, self.publish_pose)
        self.angle = 0.0

    def publish_pose(self):
        # Example: circle around origin at y=5, radius=10
        self.angle += 0.01
        x = 10.0 * (rclpy.clock.Clock().now().nanoseconds / 1e9) % (2 * 3.14159)
        pose = Pose()
        pose.position.x = 10.0 * math.cos(self.angle)
        pose.position.y = 10.0
        pose.position.z = 10.0 * math.sin(self.angle)
        # rotate around x-axis 90 degrees
        pose.orientation.x = 0.7071  # cos(45 degrees)
        pose.orientation.y = 0.0
        pose.orientation.z = 0.0
        pose.orientation.w = 0.7071  # sin(45 degrees)
        self.pub.publish(pose)
        self.get_logger().info(f'Published camera pose: {pose.position.x:.2f}, {pose.position.y:.2f}, {pose.position.z:.2f}')

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