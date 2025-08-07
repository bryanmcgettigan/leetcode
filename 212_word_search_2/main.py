#TODO not fast enough
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        nRow = len(board)
        nCol=len(board[0])
        path=set()

        def dfs(r,c,i,word):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=nRow or c>=nCol or word[i]!=board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))

            result = dfs(r,c+1,i+1,word) or dfs(r,c-1,i+1,word) or dfs(r-1,c,i+1,word) or dfs(r+1,c,i+1,word)

            path.remove((r,c))

            return result
        rList=[]
        for word in words:
            for row in range(nRow):
                for col in range(nCol):
                    if dfs(row,col,0,word):
                        rList.append(word)
                        break
                if word in rList:
                    break


        return rList
        



solution=Solution()
board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words=["oath","pea","eat","rain"]
print(solution.findWords(board,words))