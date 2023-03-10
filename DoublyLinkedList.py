class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
       


class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        
        else:
           
            former = self.tail.prev
            former.next = None
            temp.prev = None
            self.tail = former

    
        self.length -= 1
        print(temp.value)
        return temp.value

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            temp.prev = self.head
            self.head.next = temp

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            print("nothing here")
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
         
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            
        self.length -= 1
        print("popedfirst",temp)
        return temp

    def get(self,index):

        if index < 0 or index >= self.length:
            print("none")
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1,index,-1):
                temp = temp.prev

        print(temp)
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        before.next = new_node
        after.prev = new_node
        new_node.next = after
        new_node.prev = before

        self.length += 1
        return True

    def remove(self,index):
        if self.length == 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        else:
            removed = self.get(index)
            removed.prev.next = removed.next
            removed.next.prev = removed.prev
        

            removed.next = None
            removed.prev = None
           
            return removed



            






my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(4)
my_doubly_linked_list.insert(2,3)
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()
# print("haha")
# my_doubly_linked_list.pop()
# print("haha")
# my_doubly_linked_list.prepend(0)
# my_doubly_linked_list.print_list()
# print("haha")
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.print_list()
my_doubly_linked_list.get(1)

