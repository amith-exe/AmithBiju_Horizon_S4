import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CommandListener(Node):
    def __init__(self):
        super().__init__("command_listener")
        self.subscription = self.create_subscription(
            String,
            "rover_command",
            self.command_callback,
            10,
        )

    def command_callback(self, msg):
        self.get_logger().info(f"Received command: {msg.data}")
        if msg.data == "MOVE_FORWARD":
            self.get_logger().info("Rover wheels moving...")
        else:
            self.get_logger().info("Rover stopped.")


def main(args=None):
    rclpy.init(args=args)
    node = CommandListener()
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
