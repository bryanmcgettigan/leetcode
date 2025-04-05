
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        rList = []
        queue=[]

        queue.append(root)
        while queue:
            cList=[]
            n=len(queue)
            for _ in range(0,n):
                cNode = queue.pop(0)
                if cNode:
                    cList.append(cNode.val)
                    queue.append(cNode.left)
                    queue.append(cNode.right)

            if cList:
                rList.append(cList)
        
        return rList

        
solution = Solution()

n = TreeNode(1)
n.left=TreeNode(2)
n.right=TreeNode(3)
n.left.left=TreeNode(4)
n.right.right=TreeNode(5)

print(solution.levelOrder(n))