class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0

        left = 0
        right=len(height)-1
        while left<right:
            cArea = (right-left)*min(height[right],height[left])
            if cArea>maxArea:
                maxArea = cArea
            
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
    
        
        
        return maxArea



solution=Solution()

height=[1,1]

print(solution.maxArea(height))