import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


# This node publishes random distance values every second.
class DistancePublisher(Node):
    def __init__(self):
        super().__init__("distance_publisher")
        # Create a publisher on the "distance" topic.
        self.publisher_ = self.create_publisher(Int32, "distance", 10)
        # Call timer_callback once every second.
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        # Generate a random number to simulate a sensor reading.
        msg.data = random.randint(1, 100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing distance: "{msg.data}"')


def main(args=None):
    # Initialize ROS 2 communication.
    rclpy.init(args=args)
    node = DistancePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up the node before shutting down ROS 2.
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
