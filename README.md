# **iRobot Create-3 Navigation Project**

![iRobot Create-3](images/create3_banner.png)

## **Table of Contents**

- [Introduction](#introduction)
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
- [Extra Features](#extra-features)
- [Video Demonstration](#video-demonstration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## **Introduction**

This project demonstrates the autonomous navigation of the iRobot Create-3 robot in a simulated environment using ROS 2 and Gazebo. The robot undocks from its docking station, follows a creative trajectory from point A to point B based on waypoints, and optionally returns to dock.

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
   git clone https://github.com/your_username/create3_navigation.git```

2. **Set Up the Workspace:**

   ```bash
  mkdir -p ~/create3_ws/src
  cd ~/create3_ws/src
  git clone https://github.com/iRobotEducation/create3_sim.git -b humble
  cp -r ~/create3_navigation/create3_controller ./```

3. **Install Dependencies:**

   ```bash
  cd ~/create3_ws/
  rosdep update
  rosdep install --from-paths src --ignore-src -r -y```

4. **Build the Workspace:**
   ```bash
  colcon build```

5. **Source the Workspace:**
   ```bash
  source install/setup.bash```


## **Project Structure**

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



## **Nodes Description**