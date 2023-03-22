

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

    
  

class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def insert(self, value: int) -> int:
        newNode = Node(value)

        if (self.head == None and self.tail == None):
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode


    def print(self):

        # no nodes
        if (self.head == None):
            print("head--> <--tail")
            return


        print("head--> ", end="")

        # one node
        if (self.head == self.tail):
            print(f"{self.head.value} <--tail")
            return

        # more than one nodes
        current = self.head
        while(current.next != None):
            print(current.value, end="")
            current = current.next

            if (current.next != None):
                print("--> ", end="")
        print(" <--tail")


    def delete(self, value: int):

        # no nodes
        if (self.head == None):
            return
        
        # one node
        elif (self.head == self.tail):
            del self.head
            self.head = None
            self.tail = None
            return
    
        current = self.head
        prev = None
        while(current.next != None):

            # first node
            if (self.head == self.tail and self.head.value == value ):
                del self.head
                self.head == None
                self.tail == None
                return
            
            # last node
            elif (current == self.tail):
                del prev.next
                self.tail = prev
                
        
            # middle nodes
            elif (current.value == value):
                prev.next = current.next
                del prev.next
        
            prev = current
            current = current.next

   


    def find(self, value: int):
        pass
        # current = self.head
        # while(current.next != None):
        
        #     print(f"{current.value}", end="")
        #     current = current.next

        #     if (current.next != None):
        #         return



def main():

    # creating object
    ll = SinglyLinkedList()


    # insert method 
    ll.insert(100)
    print(ll.head.value)
    # ll.insert(200)
    # ll.insert(300)
    # ll.insert(400)
    # ll.insert(500)

    # print method
    ll.print()




    ll.delete(100)
    ll.print()





if __name__ == "__main__":
    main()
        




