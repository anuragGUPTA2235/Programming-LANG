class Node:
    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev

if __name__ == "__main__":
     print("creating a two way linked list")
     node1 = Node(1,None,None)
     node2 = Node(2,None,None)
     node3 = Node(3,None,None)
     node4 = Node(4,None,None)
     node5 = Node(5,None,None)

     node1.next = node2
     node2.next = node3
     node3.next = node4
     node4.next = node5
     node5.next = node1

     node1.prev = node5
     node2.prev = node1
     node3.prev = node2
     node4.prev = node3
     node5.prev = node4

     current = node1
     counter = 0
     while current != None and counter < 5:
         print(current.data)
         current = current.next
         counter += 1

     print("from last")    

     last = node5
     while last != None and counter < 10:
         print(last.data)
         last = last.prev  
         counter = counter + 1 


     

     



