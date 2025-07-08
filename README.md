# Aerial Sim ROS2

Welcome to the **Aerial Sim ROS2** package! This package provides a ROS2 interface for simulating quadrotors with Unity.

## Getting Started

To launch the simulation, follow these steps:

1. **Start the ROS TCP Endpoint:**
   ```bash
   ros2 run ros_tcp_endpoint default_server_endpoint
   ```

2. **Run the Unity Quadrotor Control Interface:**
   ```bash
   ros2 run unity_interface quadrotor_control.py
   ```

## Description

- `ros_tcp_endpoint` enables communication between ROS2 and Unity.
- `quadrotor_control.py` manages quadrotor control commands and simulation feedback.

## Requirements

- ROS2 (tested on Humble/Foxy)
- Unity with ROS-TCP-Connector package

## Support

For questions or issues, please open an issue in this repository.

Happy simulating!