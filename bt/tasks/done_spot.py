import bt_library as btl
from ..globals import SPOT_CLEANING

class DoneSpot(btl.Task):
    """
    Implementation of the Task "Done Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Spot cleaning done")

        # update the blackboard spot_cleaning value to false
        blackboard.set_in_environment(SPOT_CLEANING, False)

        return self.report_succeeded(blackboard)
