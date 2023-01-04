import rclpy
import datetime
from rclpy.node import Node
from log_msgs.msg import Log

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Log, "message", 10) 
        node.create_timer(0.01, self.cb)
        self.cb

    def cb(self):
        
        self.n = input('Enter your message\n:')

        msg = Log()
        msg.log = self.n
        msg.time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        
        if self.n != '\n':
            self.pub.publish(msg)

        self.n = '\n'

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
