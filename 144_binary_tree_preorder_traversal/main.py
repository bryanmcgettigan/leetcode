
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        def dfs_help(root,rList):
            if root:
                rList.append(root.val)
                dfs_help(root.left,rList)
                dfs_help(root.right,rList)#
        rList=[]

        dfs_help(root,rList)

        return rList


t6=TreeNode(val=6) 
t5=TreeNode(val=5,right=t6)
t4 = TreeNode(val=4,left=t6)
t2 = TreeNode(val=2,left=t4)
t3 = TreeNode(val=3,right=t5)
t1 = TreeNode(val=1,left=t3,right=t2)



solution = Solution()
