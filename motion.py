#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
import math

class WaypointMotion(Node):
    def __init__(self):
        super().__init__('waypoint_motion')
        self.br = TransformBroadcaster(self)
        self.timer = self.create_timer(0.05, self.update)

        # Robot state
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0

        # SAFE waypoints (avoid obstacles)
        self.waypoints = [
            (1.0, -2.3),
            (3.5, -2.0),
            (2.85,  2.85),
            (0.0,  0.0)
        ]
        self.current_wp = 0

    def update(self):
        if self.current_wp >= len(self.waypoints):
            return  # STOP COMPLETELY

        gx, gy = self.waypoints[self.current_wp]

        dx = gx - self.x
        dy = gy - self.y
        dist = math.hypot(dx, dy)

        if dist < 0.05:
            self.current_wp += 1
            return

        desired_yaw = math.atan2(dy, dx)
        yaw_error = desired_yaw - self.yaw

        # Normalize angle
        yaw_error = math.atan2(math.sin(yaw_error), math.cos(yaw_error))

        # Motion
        self.yaw += 0.1 * yaw_error
        self.x += 0.05 * math.cos(self.yaw)
        self.y += 0.05 * math.sin(self.yaw)

        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'map'
        t.child_frame_id = 'base_link'
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0
        t.transform.rotation.z = math.sin(self.yaw / 2)
        t.transform.rotation.w = math.cos(self.yaw / 2)

        self.br.sendTransform(t)

def main():
    rclpy.init()
    rclpy.spin(WaypointMotion())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
