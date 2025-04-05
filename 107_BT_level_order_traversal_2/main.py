# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        rList = []
        queue=[]
        if not root:
            return rList
        
        queue.append(root)
        while queue:
            n = len(queue)
            cList=[]
            for _ in range(0,n):
                cNode=queue.pop(0)
                if cNode:
                    cList.append(cNode.val)
                    queue.append(cNode.left)
                    queue.append(cNode.right)
            
            if cList:
                rList.append(cList)
        
        return list(reversed((rList)))

                    

solution = Solution()

n = TreeNode(3)
n.left=TreeNode(9)
n.right=TreeNode(20)
n.right.left=TreeNode(15)
n.right.right=TreeNode(7)

print(solution.levelOrderBottom(n))