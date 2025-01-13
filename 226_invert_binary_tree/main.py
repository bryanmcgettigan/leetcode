
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
      if self.left:
         self.left.printTree()
      print( self.val),
      if self.right:
         self.right.printTree()

def invertTree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    dummy = TreeNode()
    if root:
       root.left,root.right = invertTree(root.right),invertTree(root.left)
       return root 

t4 = TreeNode(val=4)
t2 = TreeNode(val=2)
t3 = TreeNode(val=3)
t1 = TreeNode(val=1,left=t2,right=t3)

    

t1.printTree()
print()
print(invertTree(t1))
t1.printTree()
