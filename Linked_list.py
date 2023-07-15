# create class for setting each node with data and next pointer
class Node(object):

    def __init__(self,d,n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node
    
    def set_next(self,n):
        self.next_node=n

    def get_data(self):
        return self.data
    
    def set_data(self,d):
        self.data = d

# Create class for linked list operations
class LinkedList(object):

    def __init__(self, r= None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size
    
    def add(self,d):
        new_node = Node (d,self.root)
        self.root = new_node
        self.size +=1

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    
    def find(self,d):
        this_node = self.root
        while this_node:
            if this_node.get_data()==d:
                return d
            else:
                this_node = this_node.get_next()
        return None
    


#testing with random data

mylist = LinkedList()
mylist.add(4)
mylist.add(2)
mylist.add(8)
print(mylist.find(8))
print("size: "+str(mylist.get_size()))
mylist.remove(2)
print("size: "+str(mylist.get_size()))
print(mylist.remove(8))
print("size: "+str(mylist.get_size()))
print(mylist.find(4))



        