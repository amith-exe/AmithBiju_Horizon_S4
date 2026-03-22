import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


# This node listens to the distance topic and prints received values.
class DistanceSubscriber(Node):
    def __init__(self):
        super().__init__("distance_subscriber")
        # Subscribe to the "distance" topic.
        self.subscription = self.create_subscription(
            Int32,
            "distance",
            self.listener_callback,
            10,
        )

    def listener_callback(self, msg):
        # Show the received distance value in the terminal.
        self.get_logger().info(f"Received distance: {msg.data}")


def main(args=None):
    # Initialize ROS 2 communication.
    rclpy.init(args=args)
    node = DistanceSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Destroy the node and stop ROS 2 cleanly.
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
