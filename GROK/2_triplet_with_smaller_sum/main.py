class Solution:
  def searchTriplets(self, arr, target):
    count = 0
    # TODO: Write your code here

    n = len(arr)
    sArr=sorted(arr)
    
    for i in range(0,n-2):
      cFirst=sArr[i]
      fP=i+1
      sP=n-1
      while fP<sP:

        if (cFirst+sArr[fP]+sArr[sP])<target:
            count=count+(sP-fP)
            fP=fP+1
        elif(cFirst+sArr[fP]+sArr[sP])>=target:
          sP=sP-1


    return count
  




solution = Solution()


arr=[-1, 4, 2, 1, 3]
target_sum=5
print(solution.searchTriplets(arr,target_sum))