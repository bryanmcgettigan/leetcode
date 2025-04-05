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



def bfs_iterative(node):
    queue=[]
    queue.append(node)

    while queue:
        n=len(queue)
        for _ in range(0,n):
            nod=queue.pop(0)
            print(nod.val)    
            if nod.left:
                queue.append(nod.left)

            if nod.right:
                queue.append(nod.right)

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


#Kadane's algorithm used for largest subarray sum

def kadanes(arr):
    n=len(arr)
    maxSum=arr[0]
    cSum=0
    for current in range(0,n):
        cSum=max(cSum,0)
        cSum+=arr[current]
        maxSum=max(maxSum,cSum)
    return maxSum


#Array for testing

arr = [4,-1,2,-7,3,4]

print(kadanes(arr))

# Construct a binary tree
root = TreeNode(5)
root.left = TreeNode(3)

root.right = TreeNode(7)
root.right.right=TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

print("DFS ITERATIVE")
print(dfs(root))

print("BFS ITERATIVE")
print(bfs_iterative(root))


