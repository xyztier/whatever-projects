class SinglyNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.__next
    
    @data.setter
    def data(self, data):
        self.__data = data
        
    @next.setter
    def next(self, next):
        self.__next = next


class DoublyNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.__next
    
    @property
    def prev(self):
        return self.__prev
    
    @data.setter
    def data(self, data):
        self.__data = data
        
    @next.setter
    def next(self, next):
        self.__next = next
        
    @prev.setter
    def prev(self, prev):
        self.__prev = prev


class PriorityNode:
        
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        self.next = None
    
    @property
    def priority(self):
        return self.__priority

    @property
    def data(self):
        return self.__data
        
    @property
    def next(self):
        return self.__next

    @priority.setter
    def priority(self, priority):
        self.__priority = priority

    @data.setter
    def data(self, data):
        self.__data = data
    
    @next.setter
    def next(self, next):
        self.__next = next
