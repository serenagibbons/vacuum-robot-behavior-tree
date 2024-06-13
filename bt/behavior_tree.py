#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt.decorators
import bt_library as btl
import bt as bt

# Instantiate the behavior tree according to the assignment

tree_root = bt.composites.Priority([
    # battery sequence subtree
    bt.composites.Sequence([
        bt.BatteryLessThan30(),
        bt.FindHome(),
        bt.GoHome(),
        bt.Dock()
    ]),
    bt.composites.Selection([
        # spot cleaning sequence subtree
        bt.Sequence([
            bt.SpotCleaning(),
            btl.Timer(20, bt.CleanSpot()),
            bt.DoneSpot()
        ]),
        # general cleaning sequence subtree
        bt.Sequence([
            bt.GeneralCleaning(),
            bt.Sequence([
                bt.Priority([
                    # dusty spot sequence subtree
                    bt.Sequence([
                        bt.DustySpot(),
                        btl.Timer(35, bt.CleanSpot()),
                        bt.AlwaysFail()
                    ]),
                    # clean floor 
                    bt.decorators.UntilFails(bt.CleanFloor())
                ]),
                bt.DoneGeneral()
            ])
        ])
    ]),
    # do nothing node
    bt.DoNothing()
])