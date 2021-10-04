class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None 

''' a->b->c->d '''
''' d->c->b->a '''

def reverse(head):
    current = head
    previous = None
    temp_next = None

    while current:
        temp_next = current.next 
        current.next = previous
        previous = current
        current = temp_next

    return previous

        



