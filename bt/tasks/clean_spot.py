import bt_library as btl

class CleanSpot(btl.Task):
    """
    Implementation of the Task "Clean Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning spot")

        return self.report_succeeded(blackboard)
