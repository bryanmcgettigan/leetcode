







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
class Solution:
    def invertTree(self,root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        rRoot = root
        dummy = TreeNode()
       
        print(root.val)
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left,root.right=root.right,root.left

        return root



# Building the tree manually
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)



    
solution = Solution()
root.printTree()
print()
(solution.invertTree(root).val)
print()
root.printTree()
