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


    def front(self):
        assert self.__head, "List is empty"
        return self.__head


    def back(self):
        assert self.__head, "List is empty"
        return self.__tail