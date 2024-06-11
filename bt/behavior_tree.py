#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

import bt as bt

# Instantiate the tree according to the assignment. The following are just examples.

# Example 1:
# tree_root = btl.Timer(5, tasks.FindHome())

# Example 2:
# tree_root = composites.Selection(
#     [
#         BatteryLessThan30(),
#         FindHome()
#     ]
# )

# Example 3:
tree_root = bt.Selection(
    [
        bt.BatteryLessThan30(),
        btl.Timer(10, bt.FindHome())
    ]
)
