# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue = []
        rList= []
        if not root:
            return rList
        queue.append(root)

        while queue:
            n=len(queue)
            cList=[]
            for _ in range(0,n):
                cNode=queue.pop(0)
                if cNode:
                    cList.append(cNode.val)
                    if cNode.children != None:
                        for child in cNode.children:
                            queue.append(child)

            if cList:
                rList.append(cList)
        return rList
    
# Constructing the N-ary tree manually
root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])


solution = Solution()

print(solution.levelOrder(root))
