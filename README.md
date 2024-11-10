# **iRobot Create-3 Navigation Project**

## **Table of Contents**

- [Introduction](#introduction)
- [Video Demonstration](#video-demonstration)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Nodes Description](#nodes-description)
  - [move_robot Node](#move_robot-node)
  - [Other Nodes](#other-nodes)
- [Usage](#usage)
  - [Launching the Simulation](#launching-the-simulation)
  - [Undocking the Robot](#undocking-the-robot)
  - [Running the move_robot Node](#running-the-move_robot-node)
- [Results](#results)

- [Acknowledgements](#acknowledgements)

---

## **Introduction**

This project demonstrates the autonomous navigation of the iRobot Create-3 robot in a simulated environment using ROS 2 and Gazebo. The robot undocks from its docking station, follows a pattern trajectory from point A to point B based on waypoints, and returns to dock.

## **Video Demonstration**
A link to your video showcasing the robot's performance:

Click the image above or [here](https://www.youtube.com/watch?v=YOUR_VIDEO_ID) to watch the video.

## **Prerequisites**

Before you begin, ensure you have met the following requirements:

- **Operating System:** Ubuntu 22.04 (or compatible)
- **ROS 2 Distribution:** Humble Hawksbill
- **Python Version:** 3.8 or higher
- **Installed Packages:**
  - `irobot_create_msgs`
  - `irobot_create_gazebo_bringup`
  - `tf_transformations`
  - `ament_index_python`
  - Any other dependencies your code might have

## **Installation**

1. **Clone the Repository:**

   ```bash
   cd ~/
   git clone https://github.com/your_username/create3_navigation.git
   ```

2. **Set Up the Workspace:**

   ```bash
   mkdir -p ~/create3_ws/src
   cd ~/create3_ws/src
   git clone https://github.com/iRobotEducation/create3_sim.git -b humble
   cp -r ~/create3_navigation/create3_controller ./
   ```

3. **Install Dependencies:**

   ```bash
   cd ~/create3_ws/
   rosdep update
   rosdep install --from-paths src --ignore-src -r -y
   ```

4. **Build the Workspace:**

   ```bash
   colcon build
   ```

5. **Source the Workspace:**

   ```bash
   source install/setup.bash
   ```

## **Project Structure**

 ```bash
   create3_ws/
├── src/
│   ├── create3_sim/                # iRobot Create-3 simulation packages
│   └── create3_controller/         # Your custom control package
│       ├── config/
│       │   └── goal.yaml           # Configuration file for goal positions
│       ├── launch/
│       │   └── move_robot.launch.py # Optional launch file
│       ├── scripts/
│       │   └── move_robot.py       # Script for moving the robot
│       └── package.xml
├── install/
├── build/
└── log/
   ```

## **Nodes Description**

### move_robot Node

#### Purpose:
The `move_robot` node is responsible for moving the iRobot Create-3 robot from its starting position to a specified goal position using a predefined trajectory pattern.

#### Key Features:
- Reads the goal position from a YAML configuration file.
- Computes a series of waypoints based on a creative pattern.
- Controls the robot's linear and angular velocities to navigate through the waypoints.
- Implements simple proportional control for rotation and movement.

#### Parameters:
- `goal_file` (string): Path to the YAML file containing the goal position. Defaults to `config/goal.yaml` within the package if not specified.

#### How It Works:
1. **Initialization**:
   - Subscribes to `/odom` to receive odometry data.
   - Publishes to `/cmd_vel` to control robot velocities.
   - Reads the goal position from the YAML file.
2. **Trajectory Planning**:
   - Generates waypoints by scaling a predefined pattern with the goal position.
   - Stores the waypoints in a list to be sequentially followed.
3. **Movement Control**:
   - In each timer callback, computes the angle and distance to the next waypoint.
   - Rotates towards the waypoint if not facing it.
   - Moves forward when aligned with the waypoint.
   - Proceeds to the next waypoint upon reaching the current one.

#### Running the Node:

```bash
ros2 run create3_controller move_robot --ros-args -p goal_file:="/path/to/goal.yaml"
```



