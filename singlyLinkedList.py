from singleNode import singleNode
class singlyLinkedList():
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    
    @property 
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, s):
        self.__size=s
    
    def isEmpty(self):
        return self.size==0
    
    def first(self):
        return self.__head
    
    def last(self):
        return self.__tail
    
    def addFirst(self,o):
        n=singleNode(o)
        if self.isEmpty():
            self.__head=n
            self.__tail=n
        else:
            n.next=self.__head
            self.__head=n
        self.size+=1      
    
    def addLast(self,o):
        n=singleNode(o)
        if self.isEmpty():
            self.__head=n
            self.__tail=n
        else:
            self.__tail.next=n
            self.__tail=n
        self.size+=1
    
    def removeFirst(self):
        if not(self.isEmpty()):
            temp=self.__head 
            self.__head=temp.next
            temp.next=None
            self.size-=1
            return temp.data
        else:
            return None
        
    def removeLast(self):
        if self.size==1:
            self.removeFirst()
        elif self.size>1:
            temp = self.__tail 
            anterior=self.__head 
            while anterior.next!=self.__tail:
                anterior=anterior.next
            anterior.next=None
            self.__tail=anterior
            self.size-=1
            return temp.data
        else:
            return None
