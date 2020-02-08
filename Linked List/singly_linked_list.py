#Implementing singly linked list

# Represents structure for Node of the linked list having data and nextnode as members.
class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node


# LinkedList class represents Linked List and has utility functions to manipulate linkedlist.
class LinkedList:
    def __init__(self, head = None):
        self.head = head

    
    # Utility function that returns head of the linkedlist
    def get_head(self):
        return self.head

    
    # Utility function that returns size of the linkedlist; number of nodes in linkedlist
    def get_size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next_node
        return size
    
    
    # Printing linkedlist nodes; By traversing all nodes; O(n) time complexity
    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data, end = " ")
            current = current.next_node
        print("")

    # Insert node at end of linkedlist; Traversing all nodes to reach end; O(n) time complexity.
    def insert_at_end(self, data):
        new_node = Node(data, None)
        # Checking if linkedlist is empty; If yes, newnode is added at end; O(1) time complexity.
        if self.head is None:
            self.head = new_node
        # Traversing to reach end of linkedlist
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
    

    # Insert node at front/beginning of linkedlist; O(1) complexity
    def insert_at_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
    
    
    # Insert node at position given; Traverse linkedlist upto that position; O(n) time complexity
    def insert_at_mid(self, data, position):
        # Check for position beyond linkedlist size
        if position not in range(1, self.get_size() + 1):
            raise "Error inserting node. Position beyond Linked List size."
            return
        else:
            # If position refers to adding at beginning, use utility function insert_at_front()
            if position == 1:
                self.insert_at_front(data)
            # Traverse upto position
            else :
                pos = 1
                previous = self.head
                current = previous.next_node
                while current:
                    if pos == position - 1:
                        break
                    pos += 1
                    previous = previous.next_node
                    current = current.next_node

                new_node.next_node = previous.next_node
                previous.next_node = new_node


# Driver code
def main():
    # How to use above defined functions?
    # Create a linkedlist object 
    # l = LinkedList()
    # Print size of linkedlist l
    # print(l.get_size())
    # Print head of linkedlist l
    # print(l.get_head())
    # Insert new node with data 10 at end of linkedlist l
    # l.insert_at_end(10)
    # Insert new node with data 344 at front of linkedlist l
    # l.insert_at_front(344)
    # Print the linked list l
    # l.print_linked_list()
    # Insert new node with data 5 at position 2 of linkedlist l
    # l.insert_at_mid(5, 2)
   

if __name__ == "__main__":
    main()