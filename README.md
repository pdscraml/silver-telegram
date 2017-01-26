# silver-telegram
### Project #2 Group 4: Simulating a Jackal in Gazebo

### Setting Up Environment for Simulation:
 '''
$ git clone {Git repository URL}
$ cd silver-telegram/lab_two_ws
$ catkin_make
$ source /opt/ros/indigo/setup.bash
$ source ./devel/setup.bash
'''

### To Run Simulation:

Running the following command in the terminal:
* Launch Gazebo with an empty world containing a jackal
* Launch RViz
* Run the random_pub.py script
* Run the keystroke_pub.py script
* Run the decider_pub.py script

'''
$ roslaunch lab2_blank_world_launch blank_world.launch
'''

### Run a script separately:
The random_pub.py script is part of the lab_two_random_pkg package.
'''
$ rosrun lab_two_random_pkg random_pub.py
'''

The keystroke_pub.py script is part of the lab_two_key_pkg package.
'''
$ rosrun lab_two_key_pkg keystroke_pub.py
'''

The decider_pub.py script is part of the lab_two_decider_pkg package.
'''
$ rosrun lab_two_decider_pkg decider_pub.py
'''

