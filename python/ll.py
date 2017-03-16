class Node:
	def __init__(self, data):
 		self.next = None
	 	self.data = data

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, arg):
		self.data = arg

	def setNext(self, arg):
		self.next = arg



class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())



if __name__ == '__main__':
	# test = Node(12)
	# print(test.getData())
	
	myLL = LinkedList()	

	myLL.add(31)
	myLL.add(77)
	myLL.add(17)
	myLL.add(93)
	myLL.add(26)
	myLL.add(54)

	print(myLL.size())
	print(myLL.search(93))
	print(myLL.search(100))

	myLL.add(100)
	print(myLL.search(100))
	print(myLL.size())

	myLL.remove(54)
	print(myLL.size())
	myLL.remove(93)
	print(myLL.size())
	myLL.remove(31)
	print(myLL.size())
	print(myLL.search(93))




