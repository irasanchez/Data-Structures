from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            # must be opposite from enqueue in queue
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
