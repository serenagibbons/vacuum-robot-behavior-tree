
import bt_library as btl

class UntilFails(btl.Decorator):
    
    def __init__(self, child: btl.TreeNode):
        """
        Default constructor.

        :param time: Duration of the until fails
        :param child: Child associated to the decorator
        """
        super().__init__(child)
    
    """
    Implementation of the Decorator "Until Fails".
    Returns RUNNING when the child returns
    SUCCEEDED or RUNNING. It returns SUCCEEDED when the
    child returns FAILED
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Running until failure")

        # Evaluate the child
        result_child = self.child.run(blackboard)

        # If the child failed, terminate immediately the timer
        if result_child == btl.ResultEnum.SUCCEEDED or result_child == btl.ResultEnum.RUNNING:
            return self.report_running(blackboard)

        return self.report_succeeded(blackboard)