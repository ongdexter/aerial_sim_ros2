# Aerial Sim ROS2

Welcome to the **Aerial Sim ROS2** package! This package provides a ROS2 interface for simulating quadrotors with Unity.

## Getting Started

To launch the simulation, follow these steps:

1. **Start the ROS TCP Endpoint and simulator:**
   ```bash
   ros2 launch sim.launch.py
   ```

2. **Communication over ROS:**
   - **Pose commands**: Send pose commands to the quadrotor on `/quadrotor/pose_cmd` (Pose msg).
   - **RGB Images**: Get images from the quadrotor on `/quadrotor/image` (Image msg, rgb8).
   - **Depth Images**: Get depth images from the quadrotor on `/quadrotor/depth` (Image msg, 16UC1, millimeters).
   - **Current pose** Get pose of the quadrotor on `/quadrotor/pose` (PoseStamped msg).

## Requirements

- ROS2 (tested on Humble)
