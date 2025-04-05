#TODO


class Solution(object):
    def exist(self, board, word):
        nRow = len(board)
        nCol=len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if r<0 or c<0 or r>=nRow or c>= nCol or word[i]!=board[r][c] or (r,c) in path:
                return False
            path.add((r,c))

            result = dfs(r,c+1,i+1) or dfs(r,c-1,i+1) or dfs(r+1,c,i+1) or dfs(r-1,c,i+1)
            path.remove((r,c))

            return result
        for row in range(nRow):
            for col in range(nCol):
                if dfs(row,col,0):
                    return True

        return False





                
                
        

    
solution=Solution()

board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCCED"

print(solution.exist(board,word))