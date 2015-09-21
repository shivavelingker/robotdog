Download file and run using Python 2.7. You will need PIL (Python Imaging Library) for the program to run.

Goal of the Python program was to allow quick and easy traversal through a map. The map is modeled after a city:
-White "shoulders" of the road indicate that the robot can proceed at a normal speed.
-Yellow shoulder indicate reduced speed.
-Red lines are equivalent to stop signs.
-Blue lines represent parking stops. To "park" click on the letter of the parking spot.

To undo a mistake, use Ctrl+Z.
Each node must be traversed one by one. If you attempt to click on a node that is invalid (such as trying to enter a one-way road from the wrong side of the wrong), you will receive an error message.

As each node is clicked, the IDLE window will display the C++ function associated with the path. Once the picture of the map is manually exited, the program will compile all the necessary code into the newCode.c file and display the same code on the IDLE screen for safety. The C file can then be downloaded onto the Lego Mindstorms robot.

Python interface written independently. C++ functions written in conjunction with friend, Lloyd Poincot.