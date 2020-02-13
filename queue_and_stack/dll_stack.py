from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        # Step 1. Increase the size to make room for adding a new tail.
        # Note: It's okay to add from the head, just be consistent
        self.size += 1
        # Use add_to_head method
        self.storage.add_to_head(value)

    def pop(self):
        pass

    def len(self):
        pass
