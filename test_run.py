class node:

    def __init__(self, data=None, nextNode = None):
        self.data = data
        self.nextNode = nextNode


class linkedlist:

    def __init__(self):
        self.head = node(17)

    def addNode(self, data):
        newNode = node(data, None)
        currentNode = self.head
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = newNode

    def print(self):
        currentNode = self.head
        while currentNode.nextNode != None:
            print(currentNode.data)
            currentNode = currentNode.nextNode


linkedlist = linkedlist()

linkedlist.addNode(10)
linkedlist.addNode(25)
linkedlist.addNode(30)

linkedlist.print()
