class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start=0
        end = len(nums)-1

        mid=0
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return end+1



solution = Solution()
nums = [1,3,5,6]
target = 0

print(solution.searchInsert(nums,target))