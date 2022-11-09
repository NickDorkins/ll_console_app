from node import Node as n

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        current = self.head

        if current is None:
            self.head = n(value)

        while current:
            if current.next is None:
                node = n(value)
                current.next = node
                return
            else:
                current = current.next