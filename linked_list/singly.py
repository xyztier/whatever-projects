from node import Node


class Singly:

    # Initialize Singly Linked List with no Nodes.
    def __init__(self):
        self.__head = None
    

    ## Add a Node at the beginning of the list.
    def add_first(self, data):
        
        # Create a new Node instance/object.
        node = Node(data)

        # If the list has Nodes,
        if self.__head:
            
            # Set the new Node's pointer to the current head.
            node.next = self.__head

        # The list's head is now the new Node.
        self.__head = node


    ## Add a Node before the first Node that has the value of `key`.
    def add_before(self, key, data):

        # Initialize traversal variable.
        current = self.__head

        # If the list's head Node has the value of key,
        # add the Node at the beginning of the list.
        if current.data == key:
            self.add_first(data)

        # If the list's head Node does not have the value of `key`,
        # proceed with traversal.
        else:

            # Creat a new Node instance/object. 
            new_node = Node(data)

            # Initialize traversal variable;
            # keeps track of the Node before `current`.
            previous = None

            # Loop while the `key` is yet to be found.
            while current.data != key:

                # Update the `previous` Node to be the `current` Node
                # before updating the current Node.
                previous = current

                # Update `current` Node to be the next Node.
                current = current.next

                # Assert error if all Nodes have been traversed (Node is None/null/void),
                # but no Node has the value of `key`.
                assert current, "Key not found"

            # Set the `previous` Node's pointer to the new Node.
            previous.next = new_node

            # Set the new Node's pointer to the Node that has value `key`.
            new_node.next = current


    ## Add a Node at the end of the list.
    def add_last(self, data):

        # Create a new Node instance/object. 
        node = Node(data)

        # If the list is empty (it has no Nodes),
        if not self.__head:

            # Set the list's head to be the new Node.
            # You could probably call `self.add_first(data)` here,
            # but that seems excessive, especially since you already
            # created the new Node instance.
            # Calling `self.add_first(data)` would mean you'll create
            # two Node instances.
            self.__head = node

        # If the list has Nodes,
        else:

            # Initialize traversal variable.
            current = self.__head

            # Loop until the last Node is reached.
            while current.next:

                # Update `current` Node to be the next Node.
                current = current.next

            # Set the last Node's pointer to the new Node.
            current.next = node


    ## Delete the Node at the beginning of the list.
    def delete_first(self):

        # Assert error if the list has no Nodes.
        assert self.__head, "List is empty"

        # Change the list's new head Node
        # from the deleted Node to the deleted Node's next Node.
        self.__head = self.__head.next
    

    ## Delete the Node at the end of the list.
    def delete_last(self):
    
        # Assert error if the list has no Nodes.
        assert self.__head, "List is empty"
        
        # Initialize traversal variable.
        current = self.__head
        
        # Initialize traversal variable;
        # keeps track of the Node before `current`.
        previous = None
        
        # Loop until the last Node is reached.
        while current.next:
            
            # Update the `previous` Node to be the `current` Node
            # before updating the current Node.
            previous = current

            # Update `current` Node to be the next Node.
            current = current.next
        
        # Set the `previous` Node's pointer to be None/null/void;
        # unchains the last Node from the rest of the list.
        previous.next = None


    ## Returns the value of each Node in the list as a single String.
    def display(self):
        
        # Assert error if the list has no Nodes.
        assert self.__head, "List is empty"
        
        # Initialize traversal variable.
        current = self.__head
        
        # Initialize the return value.
        output = ""
        
        # Loop through all Nodes in the list.
        while current:
            
            # Concatenate the value stored in the current Node to the `output` String.
            output += str(current.data) + " "
            
            # Update `current` Node to be the next Node.
            current = current.next
        
        # Remove trailing whitespaces from both sides.
        return output.strip()
    
    
    ## Returns the Node at the beginning of the list.
    def front(self):
        
        # Assert error if the list has no Nodes.
        assert self.__head, "List is empty"
        
        # Return the value stored in the head Node.
        return self.__head.data 
    
    
    ## Returns the Node at the end of the list.
    def rear(self):
        
        # Assert error if the list has no Nodes.
        assert self.__head, "List is empty"
        
        # Initialize traversal variable.
        current = self.__head
        
        # Loop until the last Node is reached.
        while current.next:
            
            # Update `current` Node to be the next Node.
            current = current.next
            
        # Return the value stored in the last Node.
        return current.data
