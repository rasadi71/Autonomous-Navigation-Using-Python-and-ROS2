#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

class Obstacles(Node):
    def __init__(self):
        super().__init__('obstacles')
        self.pub = self.create_publisher(MarkerArray, 'visualization_marker_array', 10)
        self.timer = self.create_timer(1.0, self.publish)

    def publish(self):
        markers = MarkerArray()

        # Moved obstacle_list and the loop inside the publish function
        obstacle_list = [
            # walls
            (1,  2.0,  0.0, 0.5, 0.3, 4.0, 1.0),
            (2, -2.0,  0.0, 0.5, 0.3, 4.0, 1.0),

            # blocks
            (3,  0.0,  2.0, 0.5, 1.0, 1.0, 1.0),
            (4, 0.0, -2.0, 0.5, 1.0, 1.0, 1.0),
            # random obstacles
            (6, -1.5, -1.5, 0.5, 0.6, 0.6, 0.6),
            (7,  2.5, -1.0, 0.5, 0.5, 0.5, 0.5),
            (5, 1.5, 1.5, 0.5, 0.2, 0.2, 0.2),
        ]

        for obs in obstacle_list:
            m = Marker()
            m.header.frame_id = 'map'
            m.header.stamp = self.get_clock().now().to_msg()

            m.id = obs[0]
            m.type = Marker.CUBE
            m.action = Marker.ADD

            # Map the tuple values to the Marker properties
            m.pose.position.x = obs[1]
            m.pose.position.y = obs[2]
            m.pose.position.z = obs[3]

            m.scale.x = obs[4]
            m.scale.y = obs[5]
            m.scale.z = obs[6]

            # Set color to Red
            m.color.r = 1.0
            m.color.g = 0.0
            m.color.b = 0.0
            m.color.a = 1.0

            markers.markers.append(m)

        # Publish the full array
        self.pub.publish(markers)

def main():
    rclpy.init()
    node = Obstacles()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()