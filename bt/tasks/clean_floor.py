import bt_library as btl
import random

class CleanFloor(btl.Task):
    """
    Implementation of the Task "Clean Floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning floor")

        # Simulate low probability of failure by generating a random float between 0-1
        if random.random() >= 0.9:
            return self.report_failed(blackboard)
        
        return self.report_succeeded(blackboard)
