#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TurtleCircle(Node):
    def __init__(self):
        super().__init__('turtle_circle')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer_period = 0.01
        self.timer = self.create_timer(self.timer_period, self.move)
        self.angle_turned = 0.0

        self.radius = 1.0
        self.linear_speed = 1.0
        self.angular_speed = 1.0
        self.state = 'left'

    def move(self):
        msg = Twist()
        msg.linear.x = self.linear_speed

        if self.state == 'left':
            msg.angular.z = self.angular_speed
        elif self.state == 'right':
            msg.angular.z = -self.angular_speed

        self.angle_turned += self.angular_speed * self.timer_period

        if self.angle_turned >= 2 * math.pi:
            self.angle_turned = 0
            msg.angular.z = 0.0

            if self.state == 'right':
                self.state = 'left'
            elif self.state == 'left':
                self.state = 'right'

        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleCircle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

