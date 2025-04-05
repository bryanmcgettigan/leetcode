from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        queue=[]

        queue.append(source)
        visit=set()
        visit.add(source)
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        while queue:
            vertice = queue.pop(0)
            if destination ==vertice:
                return True
            for nei_node in graph[vertice]:
                if nei_node not in visit:
                    visit.add(nei_node)
                    queue.append(nei_node)
        return False
            
                
n = 6
edges =[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
source = 7
destination = 5

solution = Solution()

print(solution.validPath(n,edges,source,destination))