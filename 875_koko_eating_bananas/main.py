class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def feasible(k):
            index=0
            cNum=piles[index]
            hours_taken=0
            while index<len(piles):

                if cNum<=0:
                    cNum=piles[index]

                if hours_taken>h:
                    return False
                cNum=cNum-k

                if cNum<=0:
                    index=index+1

                hours_taken=hours_taken+1
            return hours_taken<=h
        
        end = max(piles)
        start=1

        while start<end:

            mid = (start+end)//2
            print(mid)
            if feasible(mid):
                end = mid
            else:
                start=mid+1
        return end

        
solution=Solution()


piles=[3,6,7,11]

h=8
def feasible(k):
    index=0
    cNum=piles[index]
    hours_taken=0
    while index<len(piles):

        if cNum<=0:
            cNum=piles[index]

        if hours_taken>h:
            return False
        cNum=cNum-k

        if cNum<=0:
            index=index+1

        hours_taken=hours_taken+1
    return True

print(feasible(23))
print(solution.minEatingSpeed(piles,h))