from node import Node


class Singly:
    
    def __init__(self):
        self.__head = None
    
    
    def add_first(self, data):
        node = Node(data) # new Node instance/object
        
        if self.__head: # if the linked list has a head / already has a node at the front
            node.next = self.__head
        self.__head = node


    def add_before(self, key, data):
        current = self.__head
    
        if current.data == key:
            self.add_first(data)
        else:
            new_node = Node(data)
            
            previous = None
            
            while current.data != key:
                previous = current
                current = current.next
                
                assert current, "Key not found"
                
            previous.next = new_node
            new_node.next = current


    def add_last(self, data):
        node = Node(data) # new Node instance/object
        
        if not self.__head: # if linked list has no head / no nodes
            self.__head = node
        else: # linked list has a head / nodes already
            current = self.__head
            while current.next:
                current = current.next
            
            current.next = node


    def delete_first(self):
        assert self.__head, "List is empty"
        
        self.__head = self.__head.next
    

    def delete_last(self):
        assert self.__head, "List is empty"
        
        current = self.__head
        previous = None
        
        while current.next:
            previous = current
            current = current.next
            
        previous.next = None


    def display(self):
        assert self.__head, "List is empty"
        
        current = self.__head
        output = ""
        
        while current:
            output += str(current.data) + " "
            current = current.next
            
        return output.strip()
    
    
    def front(self):
        assert self.__head, "List is empty"
        return self.__head.data 
    
    
    def rear(self):
        assert self.__head, "List is empty"
        
        current = self.__head
        while current.next:
            current = current.next
            
        return current.data
    
    
s = Singly()

s.add_first(1)
s.add_first(2)
s.add_first(3)
print(s.display())

s.add_before(3, 100)
print(s.display())

s.add_before(3, 200)
print(s.display())

s.add_first(500)