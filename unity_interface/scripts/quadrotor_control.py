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
        # do a circle centered at (5,5,20) with a radius of 10
        # and a speed of 0.05 radians per update
        self.pose.position.x = 5.0
        self.pose.position.y = -5.0
        self.pose.position.z = 20.0
        # Calculate the new position based on a circular path
        self.pose.position.x += 10.0 * math.cos(self.angle)
        self.pose.position.y += 10.0 * math.sin(self.angle)
        # Increment the angle for the next position
        self.angle += 0.02
        if self.angle >= 2 * math.pi:
            self.angle -= 2 * math.pi
              
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