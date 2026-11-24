from node import PriorityNode as Node


class PriorityQueue:
    
    def __init__(self):
        self.__front = None
        
    
    def enqueue(self, priority, data):
        new_node = Node(priority, data)
        
        if not self.__front:
            self.__front = new_node
        
        else:
            current = self.__front
            previous = None
            
            while True:
                previous = current
                current = current.next
                
                if (not current) or (current.priority > priority):
                    break
            
            new_node.next = current
            previous.next = new_node
    
    
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
    
    
    def display_priority(self):
        if not self.__front:
            return ""
        
        current = self.__front
        output = ""
        
        while current:
            output += f"[{current.priority}] "
            current = current.next
            
        return output.strip()
    
    
    def display_data(self):
        if not self.__front:
            return ""
        
        current = self.__front
        output = ""
        
        while current:
            output += f"[{current.data}] "
            current = current.next
            
        return output.strip()
    
    
    def display_all(self):
        if not self.__front:
            return ""
        
        current = self.__front
        output = ""
        
        while current:
            output += f"[{current.priority}, {current.data}] "
            current = current.next
            
        return output.strip()