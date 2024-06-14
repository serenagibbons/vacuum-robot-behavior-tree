# Behavior Trees: Vacuum Cleaning Robot

This program simulates a vacuum cleaning robot with a behavior tree and is implemented as a basic reflex agent.

## Instructions

Run the program in the command line or terminal using the command `python main.py` in the root directory of the project.

A menu is displayed in the console, prompting the user to select general cleaning, spot cleaning, or to terminate the program. The user may make a selection by typing the number corresponding to the option they would like to select, or `0` to terminate the program, and then pressing the `enter` key.

The user will be prompted for a menu selection whenever the evaluation of the behavior tree has completed and there are no more RUNNING tasks. The program will terminate once the user selects `0` and there are no more RUNNING tasks.

## Structure

The behavior tree is comprised of `Task`, `Condition`, `Composite`, and `Decorator` nodes. Each
type of node contains a `run` function that executes and returns a ResultEnum of `FAILED`, `RUNNING`, or `SUCCEEDED`.

The composite node constructors accept a list of children nodes. These composite nodes are used to construct the tree. The three types of composite nodes are:
- Priority: Evaluates children in order of priority. The priority node is implemented by iterating through the list of children nodes and must be passed an ordered list where the first child node has the highest priority and the last child node has the lowest priority. It will return FAILED if all the children have returned FAILED. It will return SUCCEEDED immediately if a child returns SUCCEEDED, or will return RUNNING immediately if a child returns RUNNING.
- Selection: Evaluates children from left to right, starting from the previous RUNNING child. It will return FAILED if all the children have returned FAILED. It will return SUCCEEDED immediately if a child returns SUCCEEDED, or will return RUNNING immediately if a child returns RUNNING.
- Sequence: Evaluates children from left to right, starting from the previous RUNNING child. It will return SUCCEEDED if all the children have returned SUCCEEDED. It will return FAILED immediately if a child returns FAILED, or will return RUNNING immediately if a child returns RUNNING.

## Overview

The robot will always check the battery level first. If the level is below 30%, it will plan a path to its charging base, go there, and start the docking procedure. After charging, the user must re-select the command for the robot to perform. If the battery is sufficient, it will start the function it was commanded to perform. Once the robot has docked, which is whenever the battery level is below 30%, it charges to 100% before prompting the user for a new command. Otherwise, the battery level decrements by 1% after every evaluation of the behavior tree.

There are two available cleaning options:
1. General cleaning: vacuum dust around the room until the battery falls under 30% or completes the task. If the dust sensor detects a particularly dirty spot, the robot will perform a 35s spot cleaning.
2. Spot cleaning: it will perform a 20s intensive cleaning in a specific area.

The Blackboard stores the state of the system. The following elements are stored in the blackboard:
- BATTERY_LEVEL: An integer number between 0 and 100
- SPOT_CLEANING: A boolean value – True if the command was requested, otherwise False
- GENERAL_CLEANING: A boolean value – True if the command was requested, otherwise False
- DUSTY_SPOT_SENSOR: A boolean value – True if the sensor detected a dusty spot during the cycle, otherwise False
- HOME_PATH: A string value - The path to the docking station

The GENERAL_cLEANING and SPOT_CLEANING blackboard values are set by the user and are reset after evaluation of the behavior tree. The DUSTY_SPOT_SENSOR value is simulated by generating a random float between 0 and 1 and setting DUSTY_SPOT_SENSOR to True if the value is >= 0.9, otherwise setting it to False.

The Clean Floor task will return RUNNING until it fails. It will return FAILED when there is nothing more to clean. The result of the task simulates a low probability of failure by generating a random float between 0 and 1 and returning FAILED if the value is >= 0.9.

The Spot Cleaning and General Cleaning return RUNNING until they have completed after the specified number of tree evaluation cycles.

If the user enters 0 to terminate the program and the battery level is at least 30%, the robot will do nothing and the program will terminate; if the battery level is under 30%, the robot will dock and then the program will terminate. 