from node import SinglyNode as Node


class CircularQueue:
    
    def __init__(self):
        self.__front = self.__rear = None
        
    
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.__front:
            self.__rear.next = new_node
            new_node.next = self.__front
            self.__rear = new_node
        else:
            self.__front = self.__rear = new_node
            
            
    def dequeue(self):
        if not self.__front:
            return None
        
        data = self.__front.data
        self.__rear.next = self.__front.next
        self.__front = self.__front.next
        
        return data

    
    def front(self):
        if self.__front:
            return self.__front.data
        else:
            return None
     
     
    def rear(self):
        if self.__rear:
            return self.__rear.data
        else:
            return None
        
        
    def display(self):
        if not self.__front:
            return ""
        
        current = self.__front
        output = ""
        
        while current:
            output += str(current.data) + " "
            current = current.next
            
            if not current or current == self.__front:
                break
            
        return output.strip()
    
    
    def is_circular(self):
        if not self.__front or not self.__rear:
            return False
        elif self.__rear.next != self.__front:
            return False
        
        current = self.__front
        
        while current:
            current = current.next
            
            if not current:
                return False
            elif current == self.__front:
                return True
            
        return False