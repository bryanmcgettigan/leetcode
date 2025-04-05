
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        queue=[]
        queue.append(root)

        while queue:
            n=len(queue)
            print(n)
            for _ in range(0,n):
                cNode=queue.pop(0)

                if cNode:
                    if cNode.left:
                        queue.append(cNode.left)

                    if len(queue)>0:
                        cNode.next=queue[0]
                    else: 
                        cNode.next=Node(0)

                    if cNode.right:
                        queue.append(cNode.right)
            if cNode:
                cNode.next=Node(0)
        return root

#SETUP

# Function to create a complete binary tree from a list
def create_tree_from_list(values):
    if not values:
        return None
    
    nodes = [Node(val) for val in values]
    for i in range(len(values) // 2):
        if 2 * i + 1 < len(values):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(values):
            nodes[i].right = nodes[2 * i + 2]
    
    return nodes[0]



# Create tree nodes
values = [1, 2, 3, 4, 5, None, 7]
nodes = [Node(val) if val is not None else None for val in values]

# Link children
for i in range(len(values) // 2):
    if nodes[i] is not None:
        if 2 * i + 1 < len(values) and nodes[2 * i + 1] is not None:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(values) and nodes[2 * i + 2] is not None:
            nodes[i].right = nodes[2 * i + 2]
root=nodes[0]



solution = Solution()

root = solution.connect(root)

queue=[]
queue.append(root)

while queue:
    n=len(queue)
    for _ in range(0,n):
        cNode=queue.pop(0)
        if cNode and cNode.next:
            print(str(cNode.val) + ": " + str(cNode.next.val))
            if cNode:
                queue.append(cNode.left)
                queue.append(cNode.right)
