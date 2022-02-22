class Node: 
    def __init__(self,data):
        self.next = None
        self.last = None
        self.data = data
    
    def printNode(self):
        print(self.data)
    
    def addNext(self,Node):
        self.next=Node
    
    def addPrevious(self,Node):
        self.previous=Node
    
    def getNext(self):
        return self.next
    
    def getData(self):
        return self.data

    def changeData(self,data):
        print("Changing data from",self.data,"to",data)
        self.data=data

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def printList(self):
        currNode=self.head
        while currNode.next != None :
            print(currNode.getData(),"=> ",end="")
            currNode = currNode.getNext()
        print(currNode.getData(),"=> [end]")
        print("End of linked list")
        
    def addNext(self,newNode):
        #self.next=Node
        if self.head == None:
            self.head=newNode
        else:
            currNode = self.head
            while currNode.next != None :
                currNode = currNode.getNext()
            currNode.addNext(newNode)
        self.len+=1
    
    def addPrevious(self,Node):
        self.previous=Node
        self.len+=1
    
    def removeLast(self):
        currNode=self.head
        if currNode==None:
            print("Nothing to remove")
        else:
            while currNode.getNext().getNext() != None :
                currNode = currNode.getNext()
            currNode.next=None

    def changeData(self,dataFrom,dataTo):
        if self.head == None:
            print("Nothing to change")
        else:
            currNode = self.head
            while currNode.next != None and currNode.getData()!=dataFrom:
                currNode = currNode.getNext()
            if currNode.getData()==dataFrom:
                currNode.changeData(dataTo)

def main():
    first = Node("first")
    second = Node("second")
    third = Node("third")
    fourth = Node("fourth")
    myLinkedList = LinkedList()
    myLinkedList.addNext(first)
    myLinkedList.addNext(second)
    myLinkedList.addNext(third)
    myLinkedList.addNext(fourth)
    myLinkedList.printList()
    myLinkedList.removeLast()
    myLinkedList.printList()

main()