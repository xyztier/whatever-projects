from node import SinglyNode as Node


class LinearQueue:
    
    def __init__(self):
        self.__front = self.__rear = None
        
        
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.__front:
            self.__rear.next = new_node
            self.__rear = new_node
        else:
            self.__front = self.__rear = new_node


    def dequeue(self):
        if not self.__front:
            return None
        
        data = self.__front.data
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
        current = self.__front
        output = ""
        
        while current:
            output += str(current.data) + " "
            current = current.next
        
        return output.strip()