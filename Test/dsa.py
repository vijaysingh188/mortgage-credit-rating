

# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize next as None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None (empty list)

    # Function to insert a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)      # Create a new node with the given data
        new_node.next = self.head  # Point the new node's next to the current head
        self.head = new_node       # Update the head to the new node

    # Function to display the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
llist = LinkedList()

# Insert some elements at the beginning
llist.insert_at_beginning(10)
llist.insert_at_beginning(20)
llist.insert_at_beginning(30)

# Print the current list
llist.print_list()  # Output: 30 -> 20 -> 10 -> None