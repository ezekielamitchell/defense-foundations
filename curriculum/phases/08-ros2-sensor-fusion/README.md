# P8 — ROS 2 and Sensor Fusion

**Status:** not started  
**Estimated duration:** 10–12 weeks at 10–15 hours/week

## Focus

ROS 2 is the autonomy middleware at the center of the stack, not just another robotics tool: it is the real-time message fabric that carries perception into navigation, fuses sensors, and connects distributed telemetry to mission logic across a robot or a fleet of them. Every defense-autonomy company in the target set runs on a ROS 2-class middleware, so fluency here is a load-bearing skill, not an elective. Build and debug complete ROS 2 systems, autonomous navigation, SLAM, and sensor fusion—including one Rust ROS 2 node so the middleware is understood at the systems level, not only through `rclpy`.

## Topics

Nodes, topics, services, actions, lifecycle, QoS, URDF, Nav2, tf2, EKF/UKF, factor graphs, visual-inertial SLAM, IMU preintegration, Gazebo/Webots/Isaac Sim, `rclpy`, and `rclrs`.

## Materials

See [ROS 2 and sensor fusion](../../../learning-materials/08-ros2-sensor-fusion/README.md).

## Evidence target

A launchable rover graph with perception in the loop, a Rust perception node, and a GPS-denied navigation failure analysis.

## Exit gate

Design a ROS graph, debug tf, tune Nav2, explain SLAM failures, and ship one Rust ROS 2 node.
