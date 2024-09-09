import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(msg):
    rospy.loginfo("Turtle pose: x=%f, y=%f", msg.x, msg.y)

# function that writes 'david'
def write_david():
    rospy.init_node('write_david', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)







if __name__ == '__main__':
    try: 
        write_david()

    except Exception as e:
        pass