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
        # Example: circle on the xy plane at z=10, radius=10
        self.angle += 0.02
        pose = Pose()
        pose.position.x = 10.0 * math.cos(self.angle)  # x-forward
        pose.position.y = 10.0 * math.sin(self.angle)  # y-left
        pose.position.z = 20.0  # z-up (constant height)
        # rotate around y-axis 90 degrees
        pose.orientation.x = 0.0
        pose.orientation.y = -0.707
        pose.orientation.z = 0.0
        pose.orientation.w = 0.7071
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