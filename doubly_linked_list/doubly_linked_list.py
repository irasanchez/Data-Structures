"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        # the value at this linked list node
        self.value = value
        # reference to the previous node in the list
        self.prev = prev
        # reference to the next node in the list
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # if the list isn't empty
        if self.length > 0:
            # 1. create node & insert before current head
            self.head.insert_before(value)
            # 2. Update self.head
            self.head = self.head.prev
            self.length += 1
        elif self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        """Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly."""

        if self.length > 0:
            retained_value = self.head.value
            new_head = self.head.next
            self.delete(self.head)
            self.head = new_head
            return retained_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's previous pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        if not self.head and not self.tail:  # empty list
            self.head = new_node
            self.tail = new_node
        else:  # insert at the end of the list (beginning of the new node)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is not self.head:
            # 1. remove
            self.delete(node)

            # 2. insert @ head
            self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.length == 0:  # deleting from empty list
            return
        elif self.head == self.tail:
            # deleting list of 1 ... self.length == 1
            self.head = None
            self.tail = None
        elif node.prev is None:
            # this node is the head, so self.head == node
            self.head = node.next
        elif node == self.tail:  # node is the tail
            self.tail = node.prev
        node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass
