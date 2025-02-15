# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    
     def depth(self):
        leftDepth=0
        rightDepth=0
        if self.left == None and self.right == None:
            return 1
        if self.left:
           leftDepth= self.left.depth() + 1
        
        if self.right:
           rightDepth= self.right.depth() + 1

        return max(leftDepth,rightDepth)





def dfs(node):
    if node:
        print(node.val)
        dfs(node.left)
        dfs(node.right)
    
def dfs_iterative(node):
    stack = []
    stack.append(node)
    while len(stack)>0:
        node=stack.pop()
        if node:
            print(node.val)
            stack.append(node.right)
            stack.append(node.left)

# Construct a binary tree
root = TreeNode(5)
root.left = TreeNode(3)

root.right = TreeNode(7)
root.right.right=TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)


print(dfs_iterative(root))