#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
import random
from bt.behavior_tree import tree_root
from bt.globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH

# Main body of the assignment
current_blackboard = btl.Blackboard()
current_blackboard.set_in_environment(BATTERY_LEVEL, 39)
current_blackboard.set_in_environment(SPOT_CLEANING, False)
current_blackboard.set_in_environment(GENERAL_CLEANING, False)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
current_blackboard.set_in_environment(HOME_PATH, "")

done = False
running = False
terminate = False

# Each cycle in this while-loop is equivalent to 1 second time
while not done:
    # Step 1: Change the environment

    # Simulate user input commands
    user_input = "" 
    while not running and user_input == "":
        print("**********************************************************")
        print("Vacuum Cleaning Robot Menu")
        print("1. General Cleaning")
        print("2. Spot Cleaning")
        print("**********************************************************")
        try:
            user_input = input("Select a cleaning option or enter 0 to quit: ")
        except:
            user_input = ""
        print()

        if user_input != str(1) and user_input != str(2) and user_input != str(0):
            print("Please select a valid response.")
            user_input = ""
        elif user_input == str(0):
            terminate = True
        elif user_input == str(1):
            current_blackboard.set_in_environment(GENERAL_CLEANING, True)
        elif user_input == str(2):
            current_blackboard.set_in_environment(SPOT_CLEANING, True)
    
    # Simulate the response of the dusty spot sensor by generating a random float between 0-1
    dusty_spot = True if random.random() >= 0.9 else False
    current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, dusty_spot)

    # Step 2: Evaluating the tree
    result = tree_root.run(current_blackboard)

    # Change battery level after tree evaluation
    battery_level = current_blackboard.get_in_environment(BATTERY_LEVEL, 0)
    
    # If battery level < 30 it must have docked and is recharged
    if battery_level < 30:
        current_blackboard.set_in_environment(BATTERY_LEVEL, 100)
    # Else decrement battery level by 1
    else:
        current_blackboard.set_in_environment(BATTERY_LEVEL, battery_level - 1)

    # Reset user selection
    current_blackboard.set_in_environment(GENERAL_CLEANING, False)
    current_blackboard.set_in_environment(SPOT_CLEANING, False)

    # Step 3: Determine if your solution must terminate
    running = result == btl.ResultEnum.RUNNING
    done = not running and terminate
    
    # print("Status: " + str(result))
    # print("Not Running: " + str(not running))
    # print("Terminate: " + str(terminate))
    # print("Done: " + str(done))
    # print()
