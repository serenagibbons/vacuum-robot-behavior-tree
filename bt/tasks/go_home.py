import bt_library as btl
from ..globals import HOME_PATH

class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Returning home")

        home = blackboard.get_in_environment(HOME_PATH, "No home found")
        if home == "No home found":
            return self.report_failed(blackboard)

        return self.report_succeeded(blackboard)
