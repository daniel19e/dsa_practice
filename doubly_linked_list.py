class DoublyLinkedListNode(object):

    def __init__(self, value):
        
        self.value = value
        self.next_node = None
        self.previous_node = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next_node = b
b.previous_node = a
b.next_node = c
c.previous_node = b
        