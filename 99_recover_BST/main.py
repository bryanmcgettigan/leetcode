#TODO
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        invalid = []

        def is_valid(root):
            if root:
                if root.left:
                    if root.left.val>=root.val:
                        invalid.append(root.left)
                if root.right:
                    if root.right.val<=root.val:
                        invalid.append(root.right)
        is_valid(root)
        
        holder=invalid[0].val
        invalid[0].val=invalid[1].val
        invalid[1].val=holder

                
        