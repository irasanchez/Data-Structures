from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our Doubly Linked List a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add an item to the back of the list
        self.size += 1  # Increase the size to make room for the item
        # This is like shift where the item gets added on the front not the back
        self.storage.add_to_head(value)

    def dequeue(self):
        pass

    def len(self):
        pass
