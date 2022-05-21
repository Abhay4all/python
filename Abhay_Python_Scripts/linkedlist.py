class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def push(self,new_data):
        new_node=Node(new_data)
        # make the next of new node as head
        new_node.next=self.head

        # move the head to point the new node
        self.head=new_node

    def push_after_node(self,prev_node,new_data):
        if prev_node is None:
            print("previous node is not define")
        else:
            new_node=Node(new_data)
            new_node.next=prev_node.next
            prev_node.next=new_node





if __name__=="__main__":
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)

    llist.head.next=second
    second.next=third

    print(type(llist))
    print(type(llist.head))
    print(type(second))
    print(type(second.data))
    print(type(second.next))

    llist.printlist()
    llist.push(45)
    llist.printlist()
    llist.push_after_node(llist.head.next,44)
    llist.printlist()








