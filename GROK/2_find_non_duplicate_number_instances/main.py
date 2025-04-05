class Solution:
  def moveElements(self, arr):
    fP=1
    lP=1
    tSwaps=1
    while lP<len(arr):
        if arr[lP-1]!=arr[lP]:
          arr[fP]=arr[lP]
          lP=lP+1
          fP=fP+1
          tSwaps=tSwaps+1
        else:
           lP=lP+1
    return fP


solution = Solution()

arr = [2, 3, 3, 3, 6, 9, 9]
print(solution.moveElements(arr))
print(arr)