import bt_library as btl

class UntilFails(btl.Decorator):
    
    """
    Implementation of the Decorator "Until Fails".
    Returns RUNNING when the child returns SUCCEEDED or RUNNING. 
    It returns SUCCEEDED when the child returns FAILED.
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Running until failure")

        # Evaluate the child
        result_child = self.child.run(blackboard)

        # If the child returned succeeded or running, return running
        if result_child == btl.ResultEnum.SUCCEEDED or result_child == btl.ResultEnum.RUNNING:
            return self.report_running(blackboard)

        # else the child failed, return succeeded
        return self.report_succeeded(blackboard)