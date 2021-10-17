class Node:
    # Define sub-nodes
    A = []
    B = []

    # Define values
    val = 0

    def __init__(self, node0, node1=None) -> None:
        self.Node0 = node0
        self.Node1 = node1

    def depth_first_search_preOrder(self, Node):
