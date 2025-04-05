import math

class Solution:
  def searchTriplet(self, arr, target_sum):
    sArr=sorted(arr)

    n=len(sArr)
    closest_sum=1000000
    for i in range(0,n-2):
      cVal = sArr[i]
      left=i+1
      right=n-1
      while left<right:
        cSum = cVal+sArr[left]+sArr[right]

        if cSum==target_sum:
          return cSum
        if abs(target_sum-cSum)<abs(target_sum-closest_sum) or  (abs(target_sum - cSum) == abs(target_sum - closest_sum) and cSum < closest_sum):
          closest_sum=cSum
        
        if cSum<target_sum:
          left=left+1
        else:
          right=right-1


    return closest_sum
  


solution = Solution()


arr=[-1, 0, 2, 3]
target_sum=3
print(solution.searchTriplet(arr,target_sum))