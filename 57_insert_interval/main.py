#TODO

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        NewList = []
        returnedList = []
        for list in intervals:
            NewList.append(list[0])
            NewList.append(list[1])

        start = newInterval[0]
        end= newInterval[1]
        for index,item in enumerate(NewList):
            if item<start and NewList[index+1]>start:
                startIndex = index+1
                returnedList.append(newInterval[start])
        for index,item in enumerate(NewList):
            if item<end and NewList[index+1]>end:
                endIndex = index+1
        print(startIndex,endIndex)

        
solution = Solution()

intervals=[[1,3],[6,9]]
newInterval=[2,5] #Output [[1,5],[6,9]] 
solution.insert(intervals,newInterval)