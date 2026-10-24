from node import DoublyNode as Node


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
   
    
    def display(self):
        assert self.__head, "List is empty"
        
        current_node = self.__head
        output = ""

        while current_node:
            output += str(current_node.data) + " "
            current_node = current_node.next_node
        
        return output.strip()


    # Doubly
    def reverse(self):
        assert self.__head, "List is empty"
        
        new_list = Doubly()
        current_node = self.__head
        
        while current_node:
            new_list.add_first(current_node.data)
            current_node = current_node.next_node
        
        return new_list


    def get_node(self, key):
        assert self.__head, "List is empty"
        
        current_node = self.__head
        
        while current_node.data != key:
            previous_node = current_node
            current_node = current_node.next_node

            if not current_node:
                raise ValueError(f"Node with key '{key}' not found")

        return current_node
