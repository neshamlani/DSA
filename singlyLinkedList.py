from requests import delete


class Node:
  data = None
  next_node = None

  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return "%s" % self.data

class LinkedList:

  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def getLength(self):
    current = self.head
    count = 0

    while current:
      count += 1
      current = current.next_node
    
    print(count)

  def displayValues(self):
    current = self.head
    list = []

    while current:
      list.append(current)
      current = current.next_node
    
    print(list)

  def prependData(self, data):
    # Adds data at the first position of ll
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

  def appendData(self, data):
    current = self.head

    while current:
      if(current.next_node == None):
        current.next_node = Node(data)
        break
      
      current = current.next_node

  def insertData(self, index, data):
    current = self.head
    count = 0

    while current:
      if(count == index):
        new_node = Node(data)
        next_node = current.next_node
        current.next_node = new_node
        new_node.next_node = next_node
        count += 1
      else:
        current = current.next_node
        count += 1
  
  def deleteFirst(self):
    current = self.head
    nextNode = current.next_node
    self.head = nextNode

  def deleteLast(self):
    current = self.head

    while current:
      nextNode = current.next_node
      if(nextNode.next_node == None):
        current.next_node = None
      
      current = current.next_node

  def deleteIndex(self, index):
    current = self.head
    count = 0

    while current:
      if(count == index - 1):
        nextNode = current.next_node
        current = nextNode.next_node
        count += 1
      else:
        current = current.next_node
        count += 1

l = LinkedList()
for i in range(0, 3):
  l.prependData(i)

for i in range(4, 7):
  l.appendData(i)

l.insertData(2, 7)

l.displayValues()

l.deleteFirst()

l.displayValues()

l.deleteLast()

l.displayValues()

l.deleteIndex(2)
l.displayValues()