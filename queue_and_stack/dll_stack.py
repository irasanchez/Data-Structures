from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()  # comes with all the DLL methods

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            # removing must be from same side as adding in a stack
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
