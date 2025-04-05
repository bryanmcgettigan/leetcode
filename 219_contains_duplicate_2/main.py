#TODO

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
            
        for index in range(0,len(nums)):
            testedNum=nums[index]
            print(testedNum)
            for secondindex in range(index+1,index+k+1):
                if secondindex>=len(nums):
                    return False
                if testedNum==nums[secondindex]:
                    return True
        return False
            

        


solution = Solution()

arr= [1,2,3,4,5,6,7,8,9,9]
k=2
print(solution.containsNearbyDuplicate(arr,k))