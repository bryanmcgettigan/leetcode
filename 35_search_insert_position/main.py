class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start =0 
        end = len(nums)-1

        while start<=end:
            mid=start + (end-start)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start = mid+1
            else:
                end = mid-1


        return start
        

solution = Solution()
nums=[1,3,5,6]
target=7

print(solution.searchInsert(nums,target))