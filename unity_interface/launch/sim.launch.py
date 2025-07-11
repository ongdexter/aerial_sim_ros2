from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros_tcp_endpoint',
            executable='default_server_endpoint',
            name='ros_tcp_endpoint_server',
            output='screen',
        ),
        ExecuteProcess(
            cmd=['src/aerial_sim_ros2/aerial_sim_binaries/aerial_sim.x86_64'],
            output='screen'
        ),
    ]) 