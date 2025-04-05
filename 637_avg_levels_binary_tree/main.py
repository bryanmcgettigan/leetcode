from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return []
        q = deque([root])
        rList = []

        while q:
            n=len(q)
            cList=[]
            for _ in range(0,n):
                cNode=q.popleft()
                if cNode:
                    cList.append(cNode.val)
                    q.append(cNode.left)
                    q.append(cNode.right)
            if cList:
                length = float(len(cList))
                avg = sum(cList)/length
                rList.append(avg)
        return rList

solution = Solution()

n = TreeNode(3)
n.left=TreeNode(9)
n.right=TreeNode(20)
n.left.left=TreeNode(15)
#n.right.right=TreeNode(7)

print(solution.averageOfLevels(n))
        