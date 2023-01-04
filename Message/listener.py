import rclpy
from rclpy.node import Node
from log_msgs.msg import Log

def cb(msg):
    global node
    node.get_logger().info("\n%s\n%s\n" % (msg.time, msg.log))


rclpy.init()
node = Node("listener")
sub = node.create_subscription(Log, "message", cb, 10)
rclpy.spin(node)


