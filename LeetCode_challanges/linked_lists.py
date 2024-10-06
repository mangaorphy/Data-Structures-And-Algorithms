# Node class to represent each element (node) in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # Pointer to the next node in the list

# LinkedList class to handle operations on the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list with no head node (empty list)

    # Method to add a node at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Set the new node's next to the current head
        self.head = new_node  # Set the new node as the head of the list

    # Method to add a node at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Set the new node as the next of the last node

    # Method to delete a node by value
    def delete_node(self, key):
        # If the list is empty
        if self.head is None:
            print("The list is empty")
            return

        # If the node to be deleted is the head node
        if self.head.data == key:
            self.head = self.head.next
            return

        # Traverse the list to find the node to be deleted
        current_node = self.head
        previous_node = None
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next

        # If the node was not found
        if current_node is None:
            print("Node with data", key, "not found")
            return

        # Unlink the node from the list
        previous_node.next = current_node.next

    # Method to display the linked list
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example Usage
if __name__ == "__main__":
    # Create a new linked list
    linked_list = LinkedList()

    # Insert elements
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_beginning(5)

    print("Linked List after insertions:")
    linked_list.display()

    # Delete a node
    linked_list.delete_node(20)
    print("\nLinked List after deleting 20:")
    linked_list.display()

    # Delete head node
    linked_list.delete_node(5)
    print("\nLinked List after deleting the head (5):")
    linked_list.display()

'''

Linked List after insertions:
5 -> 10 -> 20 -> 30 -> None

Linked List after deleting 20:
5 -> 10 -> 30 -> None

Linked List after deleting the head (5):
10 -> 30 -> None


'''