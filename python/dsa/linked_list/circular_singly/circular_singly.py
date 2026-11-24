### !!! NOTE !!!
### Please put this file (circular_singly.py) in the same folder and hierarchy as node.py,
### or the import may fail unless you configure Python's module search path.
from node import Node


class CircularSingly:
    
    def __init__(self):
        self.__head = self.__tail = None
    
    
    def add_first(self, data):
        new_node = Node(data)
        previous_head = self.__head # Temporarily store previous head
        
        # List isn't empty
        if self.__head:
            self.__head = new_node # Set new head
            self.__head.next_node = previous_head # Link new head to previous head
            self.__tail.next_node = self.__head # Link tail to new head
            
        # List is empty
        else:
            self.__head = self.__tail = new_node # Initialize head and tail
            self.__tail.next_node = self.__head # Link tail to head
    
    
    def add_before(self, key, data):
        current_node = self.__head

        if current_node.data == key:
            self.add_first(data)
            
        else:
            new_node = Node(data)
            previous_node = None

            while current_node.data != key:
                previous_node = current_node
                current_node = current_node.next_node

            if not current_node:
                raise ValueError("Key not found")

            previous_node.next_node = new_node
            new_node.next_node = current_node
    
    
    def add_after(self, key, data):
        current_node = self.__head
        
        while current_node.data != key:
            current_node = current_node.next_node
            
            if current_node == self.__head:
                raise ValueError("Key not found")
                
        if current_node == self.__tail:
            self.add_last(data)
        else:
            new_node = Node(data)
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
    
    
    def add_last(self, data):
        new_node = Node(data)
        previous_tail = self.__tail # Temporarily store previous tail
        
        # List isn't empty
        if self.__head:
            self.__tail = new_node # Set new tail
            previous_tail.next_node = self.__tail # Link previous tail to new tail
            self.__tail.next_node = self.__head # Link new tail to head
        
        # List is empty
        else:
            self.__head = self.__tail = new_node # Initialize head and tail
            self.__tail.next_node = self.__head # Link tail to head
        
        
    def display(self):
        assert self.__head, "List is empty"
        
        current_node = self.__head 
        output = ""

        while True:
            output += str(current_node.data) + " "
            current_node = current_node.next_node
            
            if current_node == self.__head:
                break
        
        return output.strip()


    def delete_front(self):
        assert self.__head, "List is empty"
        
        self.__head = self.__head.next_node # Set new head
        self.__tail.next_node = self.__head # Link tail to new head


    def delete(self, node):
        assert self.__head, "List is empty"
        
        current_node = self.__head
        
        if current_node == node:
            self.delete_front()
        
        else:
            previous_node = None
            
            while current_node != node:
                previous_node = current_node
                current_node = current_node.next_node

            # 98% there is much better way to do this
            if current_node.next_node == self.__head: # current_node is tail
                self.delete_back()
                
            else:
                previous_node.next_node = current_node.next_node
    
    
    def delete_back(self):
        assert self.__head, "List is empty"
        
        current_node = self.__head
        previous_node = None
        
        # Find tail's previous node
        while current_node != self.__tail:
            previous_node = current_node
            current_node = current_node.next_node
        
        self.__tail = previous_node # Set tail to previous tail's previous node
        self.__tail.next_node = self.__head # Link new tail to head


    def pop_front(self):
        assert self.__head, "List is empty"
        
        data = self.__head.data # Temporarily store the value
        self.__head = self.__head.next_node # Set new head
        self.__tail.next_node = self.__head # Link tail to new head
        
        return data


    def pop_back(self):
        assert self.__head, "List is empty"
        
        data = self.__tail.data # Temporarily store the value
        
        current_node = self.__head
        previous_node = None
        
        # Find tail's previous node
        while current_node != self.__tail:
            previous_node = current_node
            current_node = current_node.next_node  
        
        self.__tail = previous_node # Set tail to previous tail's previous node
        self.__tail.next_node = self.__head # Link new tail to head
        
        return data


    def front(self):
        assert self.__head, "List is empty"
        return self.__head


    def back(self):
        assert self.__head, "List is empty"
        return self.__tail


    def size(self):
        if not self.__head:
            return 0
        
        count = 0
        current_node = self.__head
        
        while True:
            count += 1
            current_node = current_node.next_node
            
            if current_node == self.__head:
                break
        
        return count
    

    def is_circular(self):
        assert self.__head, "List is empty"
        return self.__tail.next_node == self.__head
