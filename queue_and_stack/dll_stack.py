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
        # Remove an item from the end
        # Return new list with the last item removed from it
        # Check if the list is empty, because of it's empty you can take something off of it
        if self.size > 0:
            self.size -= 1
            # Use remove from head method from the doubly linked list
            return self.storage.remove_from_head()
        else:
            return None  # Nothing is there

    def len(self):
        return self.size  # size keeps track of the amount of nodes which is the same thing as length
