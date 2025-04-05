#TODO
from collections import deque
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        NRows=len(heights)
        NCols = len(heights[0])
        visit=set([(0,0)])
        direct = [[0,1],[1,0],[-1,0],[0,-1]]
        q=deque([(0,0,heights[0][0])]) #row,col,height
        prevHeight=1000000000
        rList=[]
        
        cList=[]
        
        while q:
            r,c,height = q.popleft()
            if min(r,c) < 0 or r>= NRows-1 or c>= NCols-1 :
                continue
            
            if prevHeight<=height:
                cList.append([r,c])

            if r == NRows-1 or c==NCols-1 and height<=prevHeight:
                rList.append(cList)


            for dr,dc in direct:
                if (r+dr,c+dc) not in visit and (r+dr)>=0 and (c+dc)>=0 :
                    prevHeight=height
                    q.append((r+dr,c+dc,heights[r+dr][c+dc]))
                    visit.add((r+dr,c+dc))

        return rList
                

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

solution = Solution()

print(solution.pacificAtlantic(heights))