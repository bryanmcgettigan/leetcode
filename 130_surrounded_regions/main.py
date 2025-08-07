class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        nrow = len(board)
        ncol=len(board[0])
        validpath =set()
        path=set()
        def isX(r,c):

            if r<0 or c<0 or r>=nrow or c>= nrow or (r,c) in path:
                return False
            if board[r][c] =="X":
                validpath.add((r,c))
                return True
            
            path.add((r,c))
            result = isX(r,c+1) and isX(r,c-1) and isX(r+1,c) and isX(r-1,c)
            path.remove((r,c))
            return result
        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] == "O":
                    if isX(row,col):
                        print("CHECKED")
                        board[row][col] == "X"
        return board


solution = Solution()
board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(solution.solve(board))