class Node:
    def __init__(self,data): #use instance vairables of data, left and right to simulate a node
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, dat):   #If the trees empty I added the node in as the route
        if(self.root == None):
           self.root = Node(dat)
        else:
            self.insert1(dat, self.root) #I now used this to check where to add the node in using recursion

    def insert1(self, dat, node):

        if(dat < node.data): #checks where we add in this value
            if(node.left is not None): #if its less we go left, if its bigger we go right
                self.insert1(dat, node.left)
            else:
                node.left = Node(dat) #keep going until we reach a null space and we add it in there
        else:
            if(node.right is not None):
                self.insert1(dat, node.right)
            else:
                node.right = Node(dat)

    def search(self, data): #this is searching for a particular node, again I used recursion
        if(self.root is not None):
            return self.search1(data, self.root) #search1
        else:
            print("No Nodes in the Tree")
            return False          #Nodes

    def search1(self, dat, node): #this checks if value were looking at is the value we are looking for
        if(dat == node.data):#if it is we are finished
            return True      #I return True if it matches
        elif(dat < node.data and node.left is not None): #if the value is less then, we go left
            self.search1(dat, node.left)
        elif(dat > node.data and node.right is not None): #or if its bigger else we go right
            self.search1(dat, node.right)

    def displayt(self):             #I used recursion here as it was far easier than other methods like using the stack etc
        if(self.root is not None):  #calls displayt1 by passing in the root value
            self.displayt1(self.root)

    def displayt1(self, node):
        if(node is not None): #if its not null I printed out  all the left nodes first then prined out the values of all the right nodes
           self.displayt1(node.left)
           print(str(node.data) + "   ")
           self.displayt1(node.right)

    def inorder(self, dat):
        if dat is not None:
            # first traverse left subtree recursively
            self.inorder(dat.left)
            # then print node when reached
            print(dat.data)
            # then either go back or traver# se right nodes
            self.inorder(dat.right)

    def preorder(self, dat):

        if dat is not None:
            # first print node
            print(dat.data)  #then traverse right subtree
            # then traverse left subtree
            self.preorder(dat.left)
            # then traverse right subtree
            self.preorder(dat.right)

    def postorder(self, dat):
        if dat is not None:
            #traverse left subtree recursivley
            self.postorder(dat.left)
            #then traverse right subtree recursivley
            self.postorder(dat.right)
            #then print node
            print(dat.data)


def main():                            #my main function inserts a binary tree and then performs checks. It then tests the inorder,preorder and postorder functions.
    tree = Tree()
    tree.insert(2)
    tree.insert(3)
    tree.insert(0)
    tree.insert(7)
    tree.insert(1)
    print("\nTree printed:\n")
    tree.displayt()
    print("--------------------------\n")
    print("Searching for 3 ",tree.search(2))
    print("Searching for 10 ",tree.search(10))
    print("Searching for -1 ",tree.search(-1))
    print("\n Tree printed inorder: \n")
    tree.inorder(tree.root)
    print("\n Tree printed preorder: \n")
    tree.preorder(tree.root)
    print("\n Tree printed postorder: \n")
    tree.postorder(tree.root)

if __name__ == '__main__':
    main()