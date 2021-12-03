class Node:

    # Define sub-nodes
    L = None
    R = None

    # Define values
    val = None

    def __init__(self, val, node_left=None, node_right=None) -> None:
        self.L = node_left
        self.R = node_right
        self.val = val
    
    # Recursive method to generate STR representation of datastruct
    def __str__(self) -> str:
        rstr = f"{self.val}| L:{self.L} <-> R:{self.R}"
        return rstr
    
    # In-place re-ordering to Binary Search Tree (BST)
    def to_BST(self):
        if self != None:
            if self.L and self.R != None:
                if self.L.val > self.R.val: # If L>R, swap 
                    self.L, self.R = self.R, self.L
                # Recursive Calls
                self.R.to_BST()
                self.L.to_BST()
        else:
            self.to_BST(self)
    
    # Transverse the Binary Tree in Pre-Order
    def traverse_pre(self, level=0, side=-1):
        if self != None:    # setup pyramid
            if side == 0:
                rstr = "\t"
            else:
                rstr = "\t"*level
            rstr += format(level) + "|"
            rstr += format(self.val) + " - "
            if self.L != None:
                rstr += self.L.transverse_pre(level+1, 0) + "\n"
            if self.R != None:
                rstr += self.R.transverse_pre(level+1, 1) + "\n"
            return rstr
        else:
            return self.transverse_pre(self)
    
    # Calculate Height of Binary tree
    #   - amount of levels
    def height(self):
        pass

    # Count the number of nodes
    def n(self):
        pass

    # Search for node in tree, return Value, Level
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
    
    # Insert Node to tree
    def insert(self, val):
        parent, level = self.search(None)   # Find empty node
        print(f"parent_val:{parent.val}")
        if parent.L == None:    # If Left node is open
            parent.L = Node(val)
            return level
        else:                   # Else use Right node
            parent.R = Node(val)
            return level
        
    # Remove node from tree, 
    #   attach subsequent nodes back to tree
    def remove(self, val):
        if self.L is not None:
            if self.L.val == val:
                tempL = self.L.L
                self.L
            else:
                pass
        if self.R is not None:
            if self.R.val == val:
                pass
            else:
                pass
            
    # Check Full Binary Tree:
    #   - every node either 0 or 2 sub-nodes
    def is_full(self):
        pass

    # Check Complete Binary Tree:
    #   - every level except last is full
    #   - last level values as LEFT as possible
    def is_complete(self):
        pass
    

def main():

    # Set up initial tree structure with values directly
    root = Node(1)
    root.R = Node(2)
    root.L = Node(3)
    root.L.L = Node(4)
    root.R.R = Node(5)
    root.L.R = Node(6)
    
    # Test Insert Method
    #root.R.L = Node(7)
    root.insert(7)
    root.insert(8)
    root.insert(9)

    # Print root depth-first string output
    print(root.traverse_pre())

    # Test BST ordering method
    root.to_BST()
    print(root.traverse_pre())

    # Test Search
    st = 6
    nd, le = root.search(st)
    print(f"n:[{nd}] level:{le}")

if __name__ == "__main__":
    main()

