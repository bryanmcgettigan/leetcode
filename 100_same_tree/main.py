# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(roota,rootb):
            if not roota and not rootb:
                return True
            if not roota or not rootb:
                return False

            if roota.val==rootb.val:
                return dfs(roota.left,rootb.left) and dfs(roota.right,rootb.right)
            return False

        return dfs(p,q)
t6=TreeNode(val=6) 
t5=TreeNode(val=5,right=t6)
t4 = TreeNode(val=4,left=t6)
t2 = TreeNode(val=2,left=t4)
t3 = TreeNode(val=3,right=t5)
t1 = TreeNode(val=1,left=t3,right=t2)

