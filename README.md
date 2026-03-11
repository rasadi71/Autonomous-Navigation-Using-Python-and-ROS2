# ROS2 Mobile Robot Navigation using Python

This project demonstrates a simple **mobile robot navigation system** built with **ROS2** and **Python**.  
The robot model is defined using a **URDF file**, while Python scripts are used for **obstacle detection** and **motion control**.

---

## 📌 Project Overview

This project includes:

- A **URDF robot model**
- ROS2 **robot_state_publisher**
- Python scripts for:
  - Obstacle detection
  - Robot motion control

The goal is to simulate a **basic autonomous navigation pipeline**.

---

## 🛠 Technologies Used

- ROS2
- Python 3
- URDF (Unified Robot Description Format)

---

## 📂 Project Structure

project_folder/
│
├── my_robot.urdf
├── obstacles.py
├── motion.py
└── README.md   

---

## ▶️ Running the Project

Run the following commands **in sequence**.

### 1️⃣ Start the Robot State Publisher

This loads the robot model and publishes robot link transforms.


Run the following commands in separate terminals to start the simulation:

# Robot Simulation Project

This repository contains the ROS 2 configuration and Python scripts to simulate robot motion and obstacle avoidance. Follow the steps below to get the environment running.

---

## 🚀 Execution Guide

Open a new terminal for each of the following steps. Ensure you have sourced your ROS 2 environment in every terminal.


```bash
ros2 run robot_state_publisher robot_state_publisher my_robot.urdf
```
```bash
rviz2
```
```bash
python3 obstacles.py
```
```bash
python3 motion.py
```
---
# Note
### ros2 run robot_state_publisher robot_state_publisher my_robot.urdf

Publishes the relationship (TF transforms) between robot links based on the URDF model.

### obstacles.py

Handles obstacle detection or simulation for the robot environment.

### motion.py

Controls the robot's movement and navigation behavior.

## Demo
Video link: https://youtube.com/shorts/TyK6NY0Q1FA?si=G1G-X5L_P6W2_mBQ
