class Solution:
  def search(self, arr, target_sum):
    # TODO: Write your code here
    sP=0
    lP=len(arr)-1
    while sP<lP:
      total=arr[sP]+arr[lP]
      if total == target_sum:
        return [sP,lP]
      if total<target_sum:
        sP=sP+1
      else:
        lP=lP-1
    return [-1, -1]
  


solution = Solution()

arr=[1,3,4,6,7]
target_sum=20
print(solution.search(arr,target_sum))