class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None
    
def cycle_check(node):
    #check if circularly linked list
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True

    return False
