# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def maxDepth(self, root):
        depth =0
        
        if root.left:
            left=maxDepth(root.left)+1
        if root.right:
            right=depth(root.right)+1
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)
        depth = depth+ max(lDepth,rDepth)+1
        return depth


root3 = TreeNode(1)
root3.right = TreeNode(2)
root3.right.right = TreeNode(3)
solution = Solution()

depth = solution.maxDepth(root3)

print(depth)