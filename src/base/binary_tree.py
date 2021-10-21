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

    def depth_first(self, level=0, side=-1):
        if self != None:
            # setup pyramid
            if side == 0:
                rstr = "\t"
            else:
                rstr = "\t"*level
            rstr += format(level) + "|"
            rstr += format(self.val) + " - "
            if self.L != None:
                rstr += self.L.depth_first(level+1, 0) + "\n"
            if self.R != None:
                rstr += self.R.depth_first(level+1, 1) + "\n"
            return rstr
        else:
            return self.depth_first(self)
    
    # Return the lowest-level parent node that has an open node, as well as the level
    def find_open(self, level=0):
        if self.L and self.R != None:
            tL, iL = self.L.find_open(level + 1)
            tR, iR = self.R.find_open(level + 1)
            if iR < iL:
                print(f"rRIHT|iL:{iL} <-> iR:{iR}")
                return tR, level
            else:
                print(f"rLEFT|iL:{iL} <-> iR:{iR}")
                return tL, level
        else:
            return self, level-1
    
    # Insert Node to tree
    def insert(self, val):
        parent, level = self.find_open()
        print(f"parent_val:{parent.val}")
        if parent.L == None:
            parent.L = Node(val)
            return level
        else:
            parent.R = Node(val)
            return level

    def search(self, term, level=0):
        if self.val == term:
            print(f"found: term:{term}, node:[{self}] level:{level}")
            return self, level
        else:
            sL = None
            sR = None
            if self.L != None:
                sL = self.L.search(term, level + 1)
            if self.R != None:
                sR = self.R.search(term, level + 1)
            if sL and sR == None:
                return None, level

    # In-Place Transform to Binary Search Tree
    def to_search_tree(self):
        if self != None:
            if self.L and self.R != None:
                # If L>R, swap
                if self.L.val > self.R.val:
                    self.L, self.R = self.R, self.L
                self.R.to_search_tree()
                self.L.to_search_tree()
        else:
            self.to_search_tree(self)


def main():
    root = Node(1)
    root.R = Node(2)
    root.L = Node(3)
    root.L.L = Node(4)
    root.R.R = Node(5)
    root.L.R = Node(6)
    
    # Test Insert Method
    #root.R.L = Node(7)
    root.insert(7)

    # Print root depth-first string output
    print(root.depth_first())
    root.to_search_tree()
    print(root.depth_first())

    # Test Search
    st = 6
    nd, le = root.search(st)
    print(f"n:[{nd}] level:{le}")

if __name__ == "__main__":
    main()

