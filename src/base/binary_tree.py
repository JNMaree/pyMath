class Node:

    # Define sub-nodes
    L = None
    R = None

    # Define values
    val = 0

    def __init__(self, val, node_left=None, node_right=None) -> None:
        self.L = node_left
        self.R = node_right
        self.val = val
    def __str__(self) -> str:
        rstr = f"{self.val}| L:{self.L}, R:{self.R}"
        return rstr

    def depth_first(self, root=None):
        if root != None:
            rstr = format(root.val) + " - "
            if root.L != None:
                rstr += root.L.depth_first()
                if root.R != None:
                    rstr += root.R.depth_first()
            # Linebreak
            rstr += "\n"
            return rstr
        else:
            return self.depth_first(self)
    
    def find_space_level(self, level=0):
        pass


def main():
    root = Node(1)
    root.L = Node(2)
    root.R = Node(3)
    root.L.L = Node(4)
    root.R.L = Node(5)

    # Print root depth-first output
    print(root.depth_first())

if __name__ == "__main__":
    main()

