import bt_library as btl
from ..globals import HOME_PATH

class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Returning home")

        # get the blackboard home_path value
        home = blackboard.get_in_environment(HOME_PATH, "")
        # if no home_path found, return failed
        if home == "":
            return self.report_failed(blackboard)

        # otherwise return succeeded
        return self.report_succeeded(blackboard)
