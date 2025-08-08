class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) ==1 and nums[0] == target:
             return [0,0]
        def binarySearchLeft(target,arr):
            start=0
            end=len(arr)
            while start<end:
                mid = (end +start) //2
                if arr[mid] ==target:
                        while arr[mid] ==target and mid>=0:
                            mid=mid-1
                        
                        return mid+1 
                elif arr[mid] < target:
                        start = mid+1
                else:
                    end = mid
            return -1
        
        def binarySearchRight(target,arr):
            start=0
            end=len(arr)
            while start<end:
                mid = (end +start) //2
                if arr[mid] ==target:
                        while  mid < len(arr) and arr[mid] ==target:
                            mid=mid+1
                        
                        return mid-1 
                elif arr[mid] < target:
                        start = mid+1
                else:
                    end = mid
            return -1
        
        result = [binarySearchLeft(target,nums),binarySearchRight(target,nums)]
        return result

    
solution = Solution()
nums = [2,2]

target= 2
print(solution.searchRange(nums,target))