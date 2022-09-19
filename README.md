# Controlling-Anki-robot-in-a-maze
step1:

(put this in a terminal)
cd catkin_ws/
source devel/setup.bash
cd --


step2:

(put this in a new terminal)
roscore

step3:

(put this in a new terminal)
roslaunch plywood_mazes maze_3_6x6.launch


step4:

(put this in a new terminal)
roslaunch anki_description put_robot_in_world.launch 


step5:
place robot in desired place

step6:

(put this in a new terminal)
rosrun advance_robotic_tutorial name.py 


