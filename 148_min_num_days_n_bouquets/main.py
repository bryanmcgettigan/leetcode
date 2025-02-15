class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def feasible(days):
            bouquetCount=0
            cBouquet=0
            for day in bloomDay:
                if day<=days:
                    cBouquet=cBouquet+1
                    if cBouquet == k:
                        bouquetCount=bouquetCount+1
                        cBouquet=0
                if day>days:
                    cBouquet=0
            return bouquetCount>=m
        
        if (m*k)>len(bloomDay):
            return -1
        
        start=1
        end = max(bloomDay)

        while start<=end:
            mid=(start+end)//2
            if feasible(mid):
                end=mid-1
            else:
                start=mid+1
        return mid
        

solution = Solution()


bloomDay=[7,7,7,7,12,7,7]
m=2
k=3

def feasible(days):
    bouquetCount=0
    cBouquet=0
    for day in bloomDay:
        if day<=days:
            cBouquet=cBouquet+1
            if cBouquet == k:
                bouquetCount=bouquetCount+1
                cBouquet=0
        if day>days:
            cBouquet=0
    return bouquetCount>=m
    
        
print(feasible(3))

print(solution.minDays(bloomDay,m,k))