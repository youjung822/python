class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, newValue): ## newValue should be an instance from Element class
        current = self.head
        if self.head: ## if it is initiated
            while current.next:
                current = current.next
            current.next = newValue
        else: ##if it is not initiated
            self.head = newValue



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print ll.head.next.value