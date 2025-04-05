# Definition for a binary tree node.#
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        rList = []
        queue = []
        if root is None:
            return queue
        queue.append(root)
        rList.append(root.val)
        while queue:
            n=len(queue)
            for _ in range(0,n):
                cNode= queue.pop(0)
                if cNode:
                    if cNode.left:
                        queue.append(cNode.left)
                    if cNode.right:
                        queue.append(cNode.right)
            if queue:
                rList.append(queue[-1].val)
        return rList

solution = Solution()

n = TreeNode(3)
n.left=TreeNode(9)
n.right=TreeNode(20)
n.left.left=TreeNode(15)
#n.right.right=TreeNode(7)

solution = Solution()

print(solution.rightSideView(n))