#TODO
# # Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        queue=[]
        hmap={}
        if not root:
            return []
        prevNode = TreeNode()
        queue.append(root)
        while queue:
            n=len(queue)

            for _ in range(0,n):
                cNode= queue.pop(0) 

                hmap[cNode.val] = hmap.get(cNode.val,0) + 1
                if cNode:
                    cNode.left.prevNode=cNode
                    queue.append(cNode.left)
                    queue.append(cNode.right)

        

t6=TreeNode(6) 
t5=TreeNode(5,right=t6)
t4 = TreeNode(val=4,left=t6)
t2 = TreeNode(val=2,left=t4)
t3 = TreeNode(val=3,right=t5)
t1 = TreeNode(val=1,left=t3,right=t2)



solution = Solution()

print(solution.distanceK(t6,5,4))