#Binary Tree #pre_order

#
#
#
#
#
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        
        self.root=Node(root)
def preorder_print(self,start,traversal):
    """Root->left->right"""
    if start:
        traversal += (str(start.value)+"-")
        traversal=self.preorder_print(start.left,traversal)
        traversal=self.preorder_print(start.right,traversal)
    return traversal
#
#
#    def print_tree(self,traversal_type):
#        if traversal_type=="preorder":
#            return self.preorder_print(tree.root,"")


#Binary Tree # In order
def inorder_print(self,start,traversal):
    """left->Root->right"""
    if start:
        traversal=self.inorder_print(start.left,traversal)
        traversal += (str(start.value)+"-")
        traversal=self.inorder_print(start.right,traversal)
    return traversal


#Binary Tree # Post order
def postorder_print(self,start,traversal):
    """left->right->Root"""
    if start:
        traversal=self.postorder_print(start.left,traversal)
        traversal=self.postorder_print(start.right,traversal)
        traversal += (str(start.value)+"-")
    return traversal




class BTNode:
    def __init__(self,val):
        self.leftNode=None
        self.rightNode=None
        self.val=val
    def insertNode(self,val):
        if self.val:
            if val< self.val:
                if self.leftNode is None :
                    self.leftNode=BTNode(val)
                else:
                    self.leftNode.insertNode(val)
            elif val>self.val:
                if self.rightNode==BTNode(val):
                    self.rightNode=BTNode(val)
                else:
                    self.rightNode.insertNode(val)





tree = BinaryTree(1)

tree.root.left = Node(2)

tree.root.right = Node(3)

tree.root.left.left = Node(4)

tree.root.left.right = Node(5)

tree.root.right.left = Node(6)

tree.root.right.right = Node(7)




def searchVal(self,data):
    if data<self.val:
        if self.leftNode is None:
            return str(data)+"is not Found in the Tree"
        return self.leftNode.searchVal(data)
    elif data >self.val:
        if self.rightNode is None:
            return str(data)+"is not found in the tree"
        return self.rightNode.searchVal(data)
    else:
        return str(self.val)+"is found in the tree"
