# Controlling-Anki-robot-in-a-maze
step1:
(put this in a terminal)
```sh
cd catkin_ws/
source devel/setup.bash
cd --
```

step2:
```sh
roscore
```
step3:
```sh
roslaunch plywood_mazes maze_3_6x6.launch
```

step4:
```sh
roslaunch anki_description put_robot_in_world.launch 
```

step5:
place robot in desired place

step6:
```sh
rosrun advance_robotic_tutorial name.py 
```

