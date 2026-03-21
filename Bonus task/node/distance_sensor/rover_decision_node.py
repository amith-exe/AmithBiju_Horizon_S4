import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class RoverDecisionNode(Node):
    def __init__(self):
        super().__init__("rover_decision_node")
        self.subscription = self.create_subscription(
            Int32,
            "distance",
            self.distance_callback,
            10,
        )
        self.command_publisher = self.create_publisher(String, "rover_command", 10)

    def distance_callback(self, msg):
        distance = msg.data
        command = "STOP" if distance < 30 else "MOVE_FORWARD"

        self.get_logger().info(f"Distance received: {distance}")

        command_msg = String()
        command_msg.data = command
        self.command_publisher.publish(command_msg)
        self.get_logger().info(f"Command published: {command}")


def main(args=None):
    rclpy.init(args=args)
    node = RoverDecisionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
