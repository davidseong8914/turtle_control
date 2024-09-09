#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

# Global variable to store the current pose of the turtle
current_pose = None

def pose_callback(msg):
    global current_pose
    # updates the current pose of the turtle
    current_pose = msg

    # prints the current pose of the turtle
    rospy.loginfo("Turtle pose: x=%f, y=%f", msg.x, msg.y)


# initializes the turtle at the top left corner
def initialize_turtle():
    global current_pose
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(30)

    while current_pose is None:
        rate.sleep()
        rospy.loginfo("Waiting for the turtle pose to be initialized")
    
    # moves the turtle to the top left corner
    while current_pose.x > 1 or current_pose.y > 1:
        twist = Twist()
        
        if current_pose.x > 1:
            twist.linear.x = -5.0
        else:
            twist.linear.x = 0.0
        
        if current_pose.y > 1:
            twist.linear.y = - 5.0
        else:
            twist.linear.y = 0.0
        
        pub.publish(twist)
        rate.sleep()
    
    # stopping the turtle
    twist = Twist()
    pub.publish(twist)
    

# function that writes 'david'
def write_david():
    rospy.init_node('write_david', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    initialize_turtle()


    # pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)



if __name__ == '__main__':
    try: 
        write_david()

    except rospy.ROSInterruptException:
        # stop turtle when script is interrupted
        # press ctrl + z to stop

        pub = ropsy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        twist = Twist()
        pub.publish(twist)
        rospy.signal_shutdown("Script interrupted")
        pass