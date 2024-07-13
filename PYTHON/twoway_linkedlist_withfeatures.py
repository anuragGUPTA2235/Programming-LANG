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

     def search(key):
         current = node1
         tail = node5
         while current != tail:
             if key == current.data:
                 print("key is present")
                 break
             else:
                 print(f"key is not present")    
             current = current.next

     def delete_pos(key):
         current = node1
         temp = current
         tail = node5
        
         while current != tail:
             if key == current.data:
                 print("found and deleted")

                 temp.next = current.next
                 current.next.prev = temp
                 break

             else:
                 print("not found")   
             temp = current
             current = current.next  

     def traverse(node1,node5):
         tail = node5
         current = node1
         while current != tail:
             print(current.data)
             current = current.next
         print()    
     
                 
                                 
     traverse(node1,node5)
     search(3)         
     delete_pos(2)
     search(2)
     traverse(node1,node5)



     

     



