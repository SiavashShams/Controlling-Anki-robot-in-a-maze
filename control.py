#!/usr/bin/env python2.7
import rospy
import time
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math
#Starts a new node
rospy.init_node('vector_controller', anonymous=True)
velocity_publisher = rospy.Publisher('/vector/cmd_vel', Twist, queue_size=1000)
vel_msg = Twist()

time.sleep(5)

x = 0.0
y = 0.0 
theta = 0.0

PI = math.pi
def PID(Kp, Ki, Kd, MV_bar=0):
    # initialize stored data
    e_prev = 0
    t_prev = -100
    I = 0
    
    # initial control
    MV = MV_bar
    
    while True:
        # yield MV, wait for new t, PV, SP
        t, PV, SP = yield MV
        
        # PID calculations
        e = SP - PV
        
        P = Kp*e
        I = I + Ki*e*(t - t_prev)
        D = Kd*(e - e_prev)/(t - t_prev)
        
        MV = MV_bar + P + I + D
        
        # update stored data for next iteration
        e_prev = e
        t_prev = t


  


def move(speed_input , distance_input, isForward_input):
    speed = int(speed_input)
    distance = int(distance_input)
    isForward = int(isForward_input)
    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    

    #Setting the current time for distance calculus
    tm0 = rospy.Time.now().to_sec()
    current_distance = 0

    #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        tm1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(tm1-tm0)
        
    #After the loop, stops the robot
    vel_msg.linear.x = 0
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)
        


def rotate(speedr_intput, angle_input, clockwise_input): #speedr,angle,clockwise):
    
    speedr = int(speedr_intput)
    angle = int(angle_input)
    clockwise = int(clockwise_input) #True or false
    
    #Converting from angles to radians
    angular_speed = speedr*2*PI/360
    relative_angle = angle*2*PI/360

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
        


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
   
 

if __name__ == '__main__':
    try:
	
	move(1,1,1)
	rotate(90,201,1)
	move(1,1,1)
	rotate(90,201,1)
	move(1,1,1)
	rotate(90,201,0)
	move(1,1,1)
	rotate(90,201,0)
	move(1,2,1)
	rotate(90,201,0)
	move(1,1,1)
	rotate(90,182,1)
	move(1,2,1)
	rotate(90,201,0)
	move(1,1,1)
	rotate(90,196,1)
	move(1,1,1)
	rotate(90,212,1)
	move(1,4,1)
	rotate(90,201,1)
	move(1,1,1)
	rotate(90,201,1)
	move(1,2,1)
	rotate(90,201,0)
	move(1,1,1)
	rotate(90,201,0)
	move(1,3,1)
	rotate(90,201,0)
	move(1,2,1)
	
	#new_odometry(1)
	#controller = PID(2, 0.1, 2)        # create pid control
	#controller.send(None)              # initialize

    except rospy.ROSInterruptException:
        pass


    


