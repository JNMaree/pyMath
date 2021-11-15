import numpy as np

class Node:
    """
        Linked List Node
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
        Simple Linked List
        Non-contiguous List of Nodes & Links
            - each Node points to next node in list

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

    # Insert a Node with value
    #   - optional position parameter
    def insert(self, value, pos=None):
        if self.__head is None: # If Head not defined
            self.__head = Node(value)
            self.__tail = self.__head
        else:
            if pos is None:     # If pos not specified, append
                next_node = Node(value)
                self.__tail.nxt = next_node
                self.__tail = next_node
            else:               # If pos specified, insert between nodes
                next_node = self.__head
                ctr = 1
                while ctr < pos and next_node is not self.__tail:
                    next_node = next_node.nxt
                    ctr += 1

                if next_node.nxt is not None:
                    over_node = next_node.nxt
                    next_node.nxt = Node(value)
                    next_node.nxt.nxt = over_node
                else:
                    next_node.nxt = Node(value)

    def search(self, value=None, pos=None):
        node = self.__head
        if value is not None:       # If value is specified,
            rpos = 0                # Return position
            while node.val != value:
                rpos += 1
                node = node.nxt
            return rpos
        elif pos is not None:       # If position is specified,
            rval = None             # Return value
            ctr = 0
            while ctr != pos:
                ctr += 1
                node = node.nxt
            rval = node.val
            return rval

    # Delete a Node by the specified value
    #   - cannot delete head node
    def delete(self, value):
        node = self.__head  
        while node.nxt is not None:
            if node.nxt.val == value:
                node.nxt = node.nxt.nxt
            node = node.nxt

    # Reverse the order of the Linked List
    def reverse(self):
        pass

def main():
    # Test Linked List methods
    ll = LinkedList()   # Create empty list
    i_count = 16

    # Test insert (append) method
    mul_insert = 2      # Append multiples of this number
    print("append | mul_ins[{}]:".format(mul_insert), end = " ")
    for i in range(i_count):
        ll.insert(i*mul_insert)
    print(ll)

    # Test delete (value) method
    mul_delete = 4      # Delete all multiples of this number
    print("delete | mul_del[{}]:".format(mul_delete), end = " ")
    for i in range(i_count//2):
        ll.delete(i*mul_delete)
    print(ll)

    # Test insert (position) method
    m = mul_delete      # Insert deleted multiples of this number
    print("insert | pos_ins[{}]:".format(m), end = " ")
    for i in range(2, i_count, 2):
        ll.insert(m, i)
        m += mul_delete
    print(ll)

if __name__ == "__main__":
    main() 
