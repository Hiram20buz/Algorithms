from utils import DoublyLinkedList
dll = DoublyLinkedList()

# Append elements to the list
dll.append(10)
dll.append(20)
dll.append(30)

# Prepend elements to the list
dll.prepend(5)
dll.prepend(1)

# Print the list
print("List after appending and prepending:")
print(dll)  # Output: 1 <-> 5 <-> 10 <-> 20 <-> 30

# Access an element by index
print("\nElement at index 2:", dll[2])  # Output: 10

# Modify an element by index
dll[2] = 15
print("\nList after modifying index 2:")
print(dll)  # Output: 1 <-> 5 <-> 15 <-> 20 <-> 30

# Insert element at index
dll.insert(3, 18)
print("\nList after inserting 18 at index 3:")
print(dll)  # Output: 1 <-> 5 <-> 15 <-> 18 <-> 20 <-> 30

# Remove an element
dll.remove(5)
print("\nList after removing 5:")
print(dll)  # Output: 1 <-> 15 <-> 18 <-> 20 <-> 30

# Get the index of an element
index = dll.index(20)
print("\nIndex of element 20:", index)  # Output: 4

# Peek at the last element
print("\nPeek at the tail:", dll.peek())  # Output: 30

# Pop the last element
popped = dll.pop()
print("\nPopped element:", popped)  # Output: 30
print("List after popping the last element:")
print(dll)  # Output: 1 <-> 15 <-> 18 <-> 20


dll = DoublyLinkedList()
dll.prepend(10)
dll.prepend(20)
dll.prepend(30)
dll.prepend(40)
print(dll)
dll.pop()
print(dll)


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
print(dll)
dll.pop_head()
print(dll)
