class Node:
    def __init__(self, value):
        self.value = value
        self.next = None




class LinkedList:

    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("nothing in the list")
            return False
        elif self.length == 1:
            self.head = None
        else:
           
            nextnum = self.head.next

            print("nextnum",nextnum)
            while nextnum:
                if nextnum.next== None:
                    print("here")
                    self.tail = self.head
                    nextnum == None
                    self.length -= 1
                
                self.head = self.head.next

                




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.pop()
my_linked_list.printList()
# print(my_linked_list.head.value)
