# Definition for a binary tree node.
class TreeNode(object):    
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def depth(root):
            left=0
            right=0
            if not root:
                return 0
            if root.left:
                left= depth(root.left) + 1
            if root.right:
                right = depth(root.right) + 1
            
            return max(left,right)

        if not root:
            return 0

        return depth(root) +1
            

root3 = TreeNode(1)
root3.right = TreeNode(2)
root3.right.right = TreeNode(3)
solution = Solution()

depth = solution.maxDepth(root3)

print(depth)