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
            return None

        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next
        
        pre.next = None
        self.tail = pre
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        print("temp",temp.value)
        return temp






        # if self.length == 0:
        #     print("nothing in the list")
        #     return False
        # elif self.length == 1:
        #     self.head = None
        # else:
        #     while self.head.next:
        #         pre = self.head 
        #         temp = pre.next

        #         if temp == None:
        #             print("last pre",pre.value)
        #             self.tail= pre
        #             self.tail.next == None
        #             print("last tail",self.tail.value)
        #             self.length -= 1
        #             return

        #         pre = temp
        #         temp = temp.next
        #         print("pre",pre.value)
        #         print("tail",self.tail.value)


            
               

                




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
# my_linked_list.pop()
my_linked_list.printList()
# print(my_linked_list.head.value)
