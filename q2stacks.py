"""Implement a queue using 2 stacks"""
class Queue2Stacks(object):
    
    def __init__(self):
        #two stacks
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()