# From scratch implementation of DLL


class DoublyLinkedList:
    class __Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = self.__Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, value):
        new_node = self.__Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop(self):
        if not self.head:
            raise IndexError("List is empty")
        datum = self.tail.data
        if self.head == self.tail:  # Only one element
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return datum

    def peek(self):
        if self.tail:
            return self.tail.data
        raise IndexError("List is empty")

    def insert(self, index, value):
        new_node = self.__Node(value)
        if index == 0:  # Insert at head
            self.prepend(value)
            return
        current = self.head
        for i in range(index - 1):
            if current is None:  # If index is out of range
                raise IndexError("Index out of range")
            current = current.next
        if current == self.tail:  # Insert at tail
            self.append(value)
        else:  # Insert in the middle
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def remove(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:  # Remove head
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:  # Remove tail
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:  # Remove in the middle
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return  # Value found and removed
            current = current.next
        raise ValueError(f"{value} not found in list")

    def index(self, value):
        current = self.head
        idx = 0
        while current:
            if current.data == value:
                return idx
            current = current.next
            idx += 1
        raise ValueError(f"{value} not found in list")

    def __getitem__(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current:
            return current.data
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current:
            current.data = value
        else:
            raise IndexError("Index out of range")

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " <-> ".join(elements)

    def pop_head(self):
        if not self.head:
            raise IndexError("List is empty")
        # datum = self.tail.data
        datum = self.head.data
        if self.head == self.tail:  # Only one element
            self.head = None
            self.tail = None
        else:
            # self.tail = self.tail.prev
            # self.tail.next = None

            self.head = self.head.next
            self.head.prev = None
        return datum
