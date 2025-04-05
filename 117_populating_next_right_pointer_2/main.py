

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



# Create tree and connect nodes
values = [1, 2, 3, 4, 5, 6, 7]
root = create_tree_from_list(values)

queue=[]
queue.append(root)

solution=Solution()


node = (solution.connect(root))




queue=[]
queue.append(root)

while queue:
    n=len(queue)
    for _ in range(0,n):
        cNode=queue.pop(0)
        print(str(cNode.val) + ": " + str(cNode.next.val))
        if cNode:
            queue.append(cNode.left)
            queue.append(cNode.right)