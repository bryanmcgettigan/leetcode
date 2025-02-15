# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        rList = []

        rList = self.inOrderTraversalHelper(root,rList)
        return rList
    
    def inOrderTraversalHelper(self,root,rList):
        if root:
            self.inOrderTraversalHelper(root.left,rList)
            rList.append(root.val)
            self.inOrderTraversalHelper(root.right,rList)
        return rList

# Construct a binary tree
root = TreeNode(5)
root.left = TreeNode(3)

root.right = TreeNode(7)
root.right.right=TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

solution = Solution()
rList = []
rList = solution.inorderTraversal(root)
print(rList)