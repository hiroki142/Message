import rclpy
import datetime
from rclpy.node import Node
from log_msgs.msg import Log

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Log, "message", 10)
        self.sub = node.create_subscription(Log, "input", self.cb, 10)

    def cb(self,msg):
        msg.time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
