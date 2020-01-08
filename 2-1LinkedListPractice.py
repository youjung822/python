"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        if self.head:
            for i in range(position-1):
                if current.next:
                    current = current.next
                else:
                    return None
            return current
        else:
            return None

    def printLinkedList(self):
        current = self.head
        if self.head:
            while current.next:
                print current.value
                current = current.next
            print current.value
        else:
            print None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        ## preTarget - Head
        if position ==1:
            new_element.next = self.head
            self.head = new_element
        else:
            preTarget = self.get_position(position - 1)
            if preTarget:
                ##Pretarget - Middle
                new_element.next = preTarget.next
                preTarget.next = new_element
            else:
                ##Pretarget - Tail
                self.append(new_element)

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        prevElem = self.head
        if self.head:
            while current.next:
                if current.value == value:
                    ## if to be deleted item is the first node
                    if prevElem == self.head:
                        self.head = current.next
                    ## if to be deleted item is the middle
                    else:
                        prevElem.next = current.next
                current = current.next
                prevElem = current


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
#ll.append(e4)
# Test get_position
# Should print 3

ll.printLinkedList()

##print ll.head.next.next.value
# Should also print 3
##print ll.get_position(0).value

# Test insert
ll.insert(e4, 4)
# Should print 4 now
#print ll.get_position(3).value
ll.printLinkedList()

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value

'''
Answer from Udacity
def get_position(self, position):
    counter = 1
    current = self.head
    if position < 1:
        return None
    while current and counter <= position:
        if counter == position:
            return current
        current = current.next
        counter += 1
    return None


def insert(self, new_element, position):
    counter = 1
    current = self.head
    if position > 1:
        while current and counter < position:
            if counter == position - 1:
                new_element.next = current.next
                current.next = new_element
            current = current.next
            counter += 1
    elif position == 1:
        new_element.next = self.head
        self.head = new_element


def delete(self, value):
    current = self.head
    previous = None
    while current.value != value and current.next:
        previous = current
        current = current.next
    if current.value == value:
        if previous:
            previous.next = current.next
        else:
            self.head = current.next
            
'''