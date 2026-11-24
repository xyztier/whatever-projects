from node import DoublyNode as Node


class Deque:
    
    def __init__(self):
        self.__front = self.__rear = None
        
    
    def enqueue_front(self, data):
        new_node = Node(data)
        
        if self.__front:
            new_node.next = self.__front
            self.__front.prev = new_node
            self.__front = new_node
        else:
            self.__front = self.__rear = new_node
    
    
    def enqueue_rear(self, data):
        new_node = Node(data)
            
        if self.__rear:
            self.__rear.next = new_node
            new_node.prev = self.__rear
            self.__rear = new_node
        else:
            self.__front = self.__rear = new_node
    
    
    def dequeue_front(self):
        if not self.__front:
            return None
        
        data = self.__front.data
        
        if self.__front.next:
            self.__front.next.prev = None
        self.__front = self.__front.next
        
        return data
    

    def dequeue_rear(self):
        if not self.__rear:
            return None
        
        data = self.__rear.data
        
        if self.__rear.prev:
            self.__rear.prev.next = None
        self.__rear = self.__rear.prev
        
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
            
        return output.strip()