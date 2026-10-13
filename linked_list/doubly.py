from node import Node


class Doubly:
    
    def __init__(self):
        self.__head = None
        
        
    def add_first(self, data):
        new_node = Node(data)
        
        if self.__head:
            new_node.next_node = self.__head # Set new node's next node to current head    
            self.__head.previous_node = new_node # Set current head's previous node to new node
        
        self.__head = new_node # Set new node as new head
    
    
    def add_before(self, key, data):
        current_node = self.__head

        if current_node.data == key:
            self.add_first(data)
            
        else:
            new_node = Node(data)

            while current_node.data != key:
                current_node = current_node.next_node

                if not current_node:
                    raise ValueError("Key not found")

            new_node.next_node = current_node
            new_node.previous_node = current_node.previous_node
            current_node.previous_node.next_node = new_node
            current_node.previous_node = new_node


    def add_after(self, key, data):
        current_node = self.__head
        
        while current_node.data != key:
            current_node = current_node.next_node
            
            if not current_node:
                self.add_last(data)
                return
                
        new_node = Node(data)
        
        new_node.previous_node = current_node
        new_node.next_node = current_node.next_node
        
        if new_node.next_node:
            new_node.next_node.previous_node = new_node
        
        current_node.next_node = new_node
    
    
    def add_last(self, data):
        new_node = Node(data)
        
        if self.__head:
            current_node = self.__head
            
            while current_node.next_node:
                current_node = current_node.next_node
                
            new_node.previous_node = current_node
            current_node.next_node = new_node
        
        # Ivan head is empty
        else:
            self.__head = new_node
        
   
    def delete_first(self):
        assert self.__head, "List is empty"
        
        self.__head = self.__head.next_node
        self.__head.previous_node = None
        
   
    def delete(self, key):
        assert self.__head, "List is empty"
        
        current_node = self.__head
        
        if current_node.data == key:
            self.delete_first()
            
        else:
            while current_node.data != key:
                current_node = current_node.next_node
                
                if not current_node:
                    raise ValueError("Key not found")
            
            current_node.previous_node.next_node = current_node.next_node
            
            if current_node.next_node:
                current_node.next_node.previous_node = current_node.previous_node
   
   
    def delete_last(self):
        assert self.__head, "List is empty"
        
        current_node = self.__head
        
        while current_node.next_node:
            current_node = current_node.next_node
    
        current_node.previous_node.next_node = None
   
    
    def display(self, reverse=False):
        assert self.__head, "List is empty"
        
        current_node = self.__head
        output = ""
        
        if reverse:
            # Traverse to last node
            while current_node.next_node:
                current_node = current_node.next_node
                
            # Do the reverse thing
            while current_node:
                output += str(current_node.data) + " "
                current_node = current_node.previous_node
                
        else:
            while current_node:
                output += str(current_node.data) + " "
                current_node = current_node.next_node
        
        return output.strip()


    def get_node(self, key):
        assert self.__head, "List is empty"
        
        current_node = self.__head
        
        while current_node.data != key:
            previous_node = current_node
            current_node = current_node.next_node

            if not current_node:
                raise ValueError(f"Node with key '{key}' not found")

        return current_node

    
doubly = Doubly()

doubly.add_first(5)
doubly.add_first(4)
doubly.add_first(3)
print("Added 3, 4, 5:\t\t", doubly.display())

doubly.add_last(6)
print("Added 6 last:\t\t", doubly.display())

doubly.delete_first()
print("Deleted first:\t\t", doubly.display())

doubly.delete_last()
print("Deleted last:\t\t", doubly.display())

doubly.add_before(5, 1)
print("Added 1 before 5:\t", doubly.display())

doubly.add_after(1, 2)
print("Added 2 after 1:\t", doubly.display())

doubly.delete(5)
print("Deleted 5:\t\t", doubly.display())

doubly.add_first(3) # 3 4 1 2
print("Added 3 first:\t\t", doubly.display())

doubly.add_last(8)
print("Added 8 last:\t\t", doubly.display())

doubly.delete(4)
print("Deleted 4:\t\t", doubly.display())

doubly.add_after(2, 6)
print("Added 6 after 2:\t", doubly.display())

doubly.add_after(1, 7)
print("Added 7 after 1:\t", doubly.display())

doubly.add_before(8, 9)
print("Added 9 before 8:\t", doubly.display())

doubly.add_after(8, 10)
print("Added 10 after 8:\t", doubly.display())

print("Reverse:\t\t", doubly.display(reverse=True))
