#TODO

class Solution:
  def searchTriplets(self, arr):
    triplets = []
    # TODO: Write your code here
    sArr=sorted(arr)
    lP=0
    rP=1
    for n in range(0,len(sArr)-2):
        current=sArr[n]
        
        lP=n+1
        rP=len(sArr)-1

        while lP<rP:
            lValue= sArr[lP]
            rValue=sArr[rP]

            if (current + lValue+rValue)==0:
                if [current,lValue,rValue] not in triplets:
                    triplets.append([current,lValue,rValue])
                lP = lP+1
                rP=rP-1
                if lP==rP:
                   break
            elif(current + lValue+rValue)<0:
                lP=lP+1
            else:
                rP=rP-1

    return triplets


arr=  [-3, 0, 1, 2, -1, 1, -2]

solution = Solution()

print(solution.searchTriplets(arr))