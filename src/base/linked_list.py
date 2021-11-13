import numpy as np

class Node:
    """
        Nodes in the list of 
    """
    # Define the value for the node
    val = ""

    # Store the next node
    nxt = None

    def __init__(self, val, nxt=None) -> None:
        self.val = val
        if nxt is not None:
            self.nxt = nxt

    def set_next(self, nxt):
        self.nxt = nxt

class LinkedList:
    """
        Sequence of Data Structures
            - Emulated using a 2D array

    """

    # Define a starting node (head)
    __head = None

    # Define a link to the end node (tail)
    __tail = None


    def __init__(self, node=None) -> None:
        if node is not None:
            if isinstance(node, (int)): # Initial value
                self.insert(node)
            elif isinstance(node, Node):    # Initial node
                self.__head = Node()

    def __str__(self) -> str:
        node = self.__head
        rst = ""
        while node is not None:
            rst += format(node.val)
            rst += ", "
            node = node.nxt
        return rst

    def insert(self, value):
        if self.__head is None: # If Head not defined
            self.__head = Node(value)
            self.__tail = self.__head
        else:                   # Else add to end of list
            next_node = Node(value)
            self.__tail.nxt = next_node
            self.__tail = next_node

    def search(self, value):
        pass
    
    def delete(self, value):
        pass


def main():
    # Test functions
    ll = LinkedList()
    ll.insert(2)
    ll.insert(4)
    ll.insert(6)
    ll.insert(8)
    print(ll)

if __name__ == "__main__":
    main() 
