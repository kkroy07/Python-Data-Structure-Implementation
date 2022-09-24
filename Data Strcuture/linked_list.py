class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    def printdata(self):
        if self.head is None:
            print("List is empty")
            return
        lst=''
        itr=self.head
        while itr:
            lst+=str(itr.data)+'->'
            itr=itr.next
        print(lst)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next=Node(data,None)
    def inser_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count=0
        ptr=self.head
        while ptr:
            count += 1
            ptr = ptr.next

        return count
    def remove(self,index):
        count = 0
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            self.insert_at_beginning(data_to_insert)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
            itr = itr.next

    def remove_by_values(self, data):
        if self.head.data == data:
            print("data found in head")
            self.head = self.head.next
        else:
            prev = None
            curr = self.head

            while curr:
                if curr.data == data:
                    prev.next = curr.next
                prev = curr
                curr = curr.next
    def middle_link_list(self):
        if self.head is None:
            return
        if self.head.next is None:
            return self.head
        slwPtr = self.head
        fastPtr = self.head
        while slwPtr and fastPtr and fastPtr.next:
            slwPtr  = slwPtr.next
            fastPtr = fastPtr.next.next
        return slwPtr

if __name__ == '__main__':
    ptr = LinkedList()
    lst=[]
    num =  int(input("Enter number of data to be inserted:"))
    for i in range(num):
        addinlist = input("Give lists data\n")
        lst.append(addinlist)
    print(lst)
    ptr.inser_values(lst)

    ptr.printdata()
    #value = input("Enter data to removed\n")
    #ptr.remove_by_values(value)
    middle = ptr.middle_link_list()
    print("Middle data is ",middle.data)



