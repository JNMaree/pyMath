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
        Simple (Single) Linked List
        Non-contiguous List of Nodes & Links
            - each Node points to next node in list
            - both Head and Tail nodes stored
    """

    # Define a starting node (head)
    __head = None

    # Define a link to the end node (tail)
    __tail = None

    def __init__(self, node=None) -> None:
        if node is not None:
            if isinstance(node, (int)):     # Initial value
                self.insert(node)
            elif isinstance(node, Node):    # Initial node
                self.__head = Node()

    def __str__(self) -> str:
        node = self.__head
        rst = ""
        while node is not None:     # Traverse loop
            rst += format(node.val)
            rst += ", "
            node = node.nxt
        return rst

    # Insert a value into the linked list
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
                if pos == 0:        # If insert to position 0
                    tmp = self.__head
                    self.__head = Node(value)
                    self.__head.nxt = tmp
                else:               # Insert to position > 0
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

    # Search the linked list for a value or position
    #   - if value specified, return position
    #   - if position specified, return value
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

    # Delete a node with the specified value
    def delete(self, value):
        node = self.__head
        if node.val == value:   # If head node to be deleted
            self.__head = node.nxt
        else:                   # Any other node to be deleted
            while node.nxt is not None:
                if node.nxt.val == value:
                    node.nxt = node.nxt.nxt
                node = node.nxt

    # Swap two node values in a linked list
    #   - specified by the position parameters
    def swap(self, posA, posB):
        nodeA = self.__head
        while posA > 0 and nodeA.nxt is not None:
            nodeA = nodeA.nxt
            posA -= 1
        nodeB = self.__head
        while posB > 0 and nodeB.nxt is not None:
            nodeB = nodeB.nxt
            posB -= 1
        # Swap values of nodes
        nodeA.val, nodeB.val = nodeB.val, nodeA.val

    # Update an existing value in the linked list to a new value
    def update(self, val, new_val):
        node = self.__head
        while node.nxt is not None and node.val != val: # Traversal loop
            node = node.nxt
        node.val = new_val 

    # Sort the elements of a linked list
    #   - uses an implementation of Bubble Sort
    def sort(self):
        changes = 1
        node = self.__head
        while changes != 0:
            changes = 0
            while node.nxt is not None:
                if node.nxt.val < node.val:
                    node.val, node.nxt.val = node.nxt.val, node.val
                    changes += 1
                else:
                    node = node.nxt
            node = self.__head

    # Reverse the order of the linked list
    #   - works by swapping values
    def reverse(self):
        pos_start = 0
        pos_end = 0
        node_end = self.__head
        while node_end.nxt is not None:
            node_end = node_end.nxt
            pos_end += 1
        while pos_start < pos_end:
            self.swap(pos_start, pos_end)
            pos_start += 1
            pos_end -= 1

    # Reverse the order of the linked list
    #   - works by swapping node.nxt's (next pointers)
    def reverse_next(self):
        node = self.__head
        while node.nxt is not None:
            tmp = node.nxt
            node.nxt.nxt = node
            node = tmp

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
    for i in range(2, i_count+1, 2):
        ll.insert(m, i)
        m += mul_delete
    print(ll)

    # Test update method
    print("update | pos_upd[{}]:".format(mul_delete), end = " ")
    for i in range(i_count):
        ll.update(i*2, i)
    print(ll)

    # Test swap method
    print("swap :".format(m), end = " ")
    for i in range(i_count//4):
        ll.swap(i_count * 2, i_count - i)
    print(ll)

    # Test reverse method
    print("rvrs :".format(m), end = " ")
    ll.reverse()
    print(ll)

    # Test reverse_next method
    print("rvr2 :".format(m), end = " ")
    ll.reverse_next()
    print(ll)

    # Test sort method
    print("sort :".format(m), end = " ")
    ll.sort()
    print(ll)

if __name__ == "__main__":
    main() 
