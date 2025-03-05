# ROS2 Turtle Beginner Project

A simple ROS2 beginner project that demonstrates how to control the TurtleSim using custom nodes to subscribe and publish messages, change the pen color, and draw a circle. To do so package is created, under this package differnt nodes are created along with ROS2 communications such as topic (publisher and subscriber), use of rqt graph to inspect how the communication works, services and clients and so on are we covered.

## Project Overview

This project includes several components, these are custom made Nodes:
- **Turtle Controller Node**: Controls the movement of the turtle in the TurtleSim environment by publishing velocity commands.
- **Pose Subscriber Node**: Subscribes to the turtle's pose and updates the turtle's drawing color.
- **Draw Circle Node**: Publishes velocity commands to make the turtle draw a circle.

This project demonstrates how to work with the ROS2 ecosystem, specifically the rclpy library, for controlling and interacting with robots.

## Prerequisites

To run this project, ensure you have the following installed:
- **ROS2 Humble** (or a compatible ROS2 version)
- **Python 3**
- **Turtlesim** (ROS2 package for simulating the turtle)

## Installation
**1. Clone the repository:**
```bash
git clone https://github.com/MinotaDache/ROS2-turtle-beginner-Project.git
cd ROS2-turtle-beginner-Project
```
**2. Build the package using** `colcon`:

Make sure you have colcon installed, which is the ROS2 build tool.
```bash
colcon build --symlink-install
```
**3. Source the workspace:**
```bash
source install/setup.bash
```
## Running the Project
**1. Launch TurtleSim:**

To run the TurtleSim, open a new terminal and execute the following:
```bash
ros2 run turtlesim turtlesim_node
```
This will launch the TurtleSim simulation where the turtle will appear on the screen.

**2. Run the Turtle Controller Node:**

In a new terminal, run the following command to control the turtle:
```bash
ros2 run my_robot_controller turtle_controller
```
This node will start controlling the turtle by publishing movement commands to `turtle1/cmd_vel`.

**3. Run the Pose Subscriber Node:**

In another terminal, run the ***Pose Subscriber*** Node to observe the turtle's pose and change the drawing color:
```bash
ros2 run my_robot_controller pose_subscriber
```
This node subscribes to the turtle1/pose topic, checks the turtle's position, and changes the drawing color based on certain conditions.
![Screenshot from 2025-03-05 20-53-19](https://github.com/user-attachments/assets/33284015-99e8-4bb5-9822-0039af5ea37b)
**4. Run the Draw Circle Node**:

Finally, in another terminal, you can run the Draw Circle Node:
```bash
ros2 run my_robot_controller draw_circle
```
This will continuously send velocity commands to make the turtle draw a circle.
![Screenshot from 2025-03-05 21-03-06](https://github.com/user-attachments/assets/715e1dee-284d-4849-a01b-b4d8909c053a)

## Project Components
**1. turtle_controller.py**

Functionality: Publishes velocity commands to control the turtle's movement.

Topic: `/turtle1/cmd_vel`

**2. pose_subscriber.py**

Functionality: Subscribes to the turtle's pose (turtle1/pose) and changes the pen color when certain conditions are met.

Topic: `/turtle1/pose`

**3. draw_circle.py**

Functionality: Sends commands to make the turtle draw a circle.

Topic: `/turtle1/cmd_vel`

**Notes**

The Pose Subscriber Node will update the turtle's pen color based on its position.
The Draw Circle Node makes the turtle continuously move in a circular path.

## Contributing

1. Fork the repository.
2. Create your feature branch (git checkout -b feature-name).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-name).
5. Create a new Pull Request.


