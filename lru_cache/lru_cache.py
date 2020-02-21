from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.order = DoublyLinkedList()
        self.storage = dict()
        self.size = 0
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # get the value out of the dictionary using the provided key
        if key not in self.storage:
            return None
        else:
            node = self.storage[key]
            self.order.move_to_end(node)
            # node.value is a tuple with a key and value inside
            return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # ^ key is the new key, do no remove it later

        # if it already exists,
        if key in self.storage:
            # overwrite the value and update the dictionary
            node = self.storage[key]
            node.value = (key, value)
            # put it at the head to mark it as most recently used
            self.order.move_to_front(node)
            return
        # if the list is full,
        if self.size == self.limit:
            # remove the oldest item

            # from the dictionary

            # self.order.tail.value[0] is the key in the storage dict
            del self.storage[self.order.tail.value[0]]
            # from the tail of DLL
            self.order.remove_from_tail()
            # update the size
            self.size -= 1
        # Add key value pair to cache - add it to the dictionary and nodes the DLL
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        # update size after adding things
        self.size += 1
