#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

# function that moves turtle1 in circles
def move_turtle_in_circles():
    # intialize 'move_turtle' node for communication with other nodes
    # anonymous=True -> assigns unique name to the node
    rospy.init_node('move_turtle', anonymous=True)

    # creates a publisher that publishes to the '/turtle1/cmd_vel' topic
    # Twist -> message type
    # queue_size -> maximum number of messages that can be stored in the publisher
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # rate at which the loop runs
    rate = rospy.Rate(10)  # 10 Hz

    # create a Twist message object (2d velocity commands [linear, angular])
    vel_msg = Twist()
    vel_msg.linear.x = 2.0  # Move forward
    vel_msg.angular.z = 1.0  # Rotate

    # run the loop until the node is stopped
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        move_turtle_in_circles()
    except rospy.ROSInterruptException:
        pass
