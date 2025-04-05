class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap = {}
        maxLHS=0
        for num in nums:
            hmap[num] = hmap.get(num,0)+1
        for num in hmap:
            maxLHS=max(maxLHS,hmap.get(num)+hmap.get(num+1,-100000))
        
        return maxLHS
        

solution = Solution()

nums=[1,3,2,2,5,2,3,7]
print(solution.findLHS(nums))