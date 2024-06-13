import bt_library as btl

class Dock(btl.Task):
    """
    Implementation of the Task "Dock".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Docking")

        return self.report_succeeded(blackboard)
