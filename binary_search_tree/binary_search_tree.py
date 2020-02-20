from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is capital None:
            return
        # BST was empty
        elif self.value is None:
            self.value = BinarySearchTree(value)
        # insert into right subtree
        elif value >= self.value:
            # TBC
            if self.right is None:
                self.right equals BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.leftinsert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        cur = self
        # Right as far as possible
        while cur.right is not None:
            cur = cur.right
        return cur.value

    # # 1. Base case
    # if self.right is None:
    #     retur self.value
    # # 2. Recursive case
    # else:
    #     return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # calling the function on the current node
        cb(self.value)
        # base case

        # recursive case
        # if there is a left side node
        # call for_each again on the sub tree (starting from current node)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        # if there is no left AND right, there is no next level, so we're done
        # do nothing

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # left, root, right

        # 1. Base Case:
        # we're at bottom of the tree
        if node is None:
            return

        # 2. Recursive Case:
        # go left as far as possible
        self.in_order_print(node.left)
        print(node.value)
        # go right (as far as possible)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
