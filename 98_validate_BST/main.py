# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        valid=True
        def is_valid(root):
            nonlocal valid
           
            if root.left:
                is_valid(root.left)
                if root.left.val>root.val:
                    valid=False

            if root.right:
                is_valid(root.right)
                if root.right.val<root.val:
                    valid=False

        is_valid(root.left)
        is_valid(root.right)

        return valid 
    
n = TreeNode(5)
n.left=TreeNode(4)
n.right=TreeNode(6)
n.right.left=TreeNode(3)
n.right.right=TreeNode(7)

solution = Solution()
print(solution.isValidBST(n))

        