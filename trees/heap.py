# balanced binary tree has roughly the same number of nodes in the left and right subtrees of the root
# create a complete binary tree (tree in which each level has all of its nodes)
# in an array representation, left child will of node at position p will be at 2p, and right child will be at 2p+1
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0