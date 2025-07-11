from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='unity_interface',
            executable='quadrotor_control.py',
            name='quadrotor_control',
            output='screen',
        ),
    ]) 