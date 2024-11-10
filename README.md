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
   git clone https://github.com/your_username/create3_navigation.git
