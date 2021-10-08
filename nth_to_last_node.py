class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None 

def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head
    
    for i in range(n-1):
        if not right_pointer.next:
            return -1
        right_pointer = right_pointer.next
    
    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next
        
    return left_pointer