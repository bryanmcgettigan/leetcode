

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        rList = []

        queue = []
        if not root:
            return rList
        queue.append(root)
        zig=False
        while queue:
            n = len(queue)
            cList=[]

            for _ in range(0,n):
                cRoot = queue.pop(0)

                if cRoot:
                    cList.append(cRoot.val)

                    queue.append(cRoot.left)
                    queue.append(cRoot.right)


            if cList:
                if zig:
                    rList.append(list(reversed(cList)))
                else:
                    rList.append(cList)
                zig = not zig


        return rList
                    


        

solution = Solution()

n = TreeNode(3)
n.left=TreeNode(9)
n.right=TreeNode(20)
n.right.left=TreeNode(15)
n.right.right=TreeNode(7)

print(solution.zigzagLevelOrder(n))