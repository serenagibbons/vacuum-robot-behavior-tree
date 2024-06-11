import bt_library as btl

class Priority(btl.Composite):
    """
    Specific implementation of the priority composite.
    """

    def __init__(self, children: btl.NodeListType):
        """
        Default constructor.

        :param children: List of children for this node
        """
        super().__init__(children)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node: 
        Children are evaluated in order of priority, ignoring any
        RUNNING child. It returns SUCCEEDED as soon as one of the children
        returns SUCCEEDED. It returns FAILED if all the children have
        returned FAILED. It will return RUNNING immediately if a child
        returns RUNNING.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        for child_position in range(len(self.children)):
            child = self.children[child_position]

            result_child = child.run(blackboard)
            if result_child == btl.ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard, 0)

            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

        return self.report_failed(blackboard, 0)
