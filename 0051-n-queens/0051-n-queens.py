class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        res=[]
        def issafe(r,c,board):
            #Up
            for i in range(r-1,-1,-1):
                if board[i][c]=="Q":
                    return False
            #lud
            row=r-1
            col=c-1
            while row>-1 and col>-1:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1
            row=r-1
            col=c+1
            while row>-1 and col<n:
                if board[row][col]=="Q":
                    return False
                row-=1
                col+=1
            return True
        def backtrack(row,n,board,res):
            if row==n:
                res.append(["".join(row) for row in board])
                return 
            for col in range(n):
                if issafe(row,col,board):
                    board[row][col]="Q"
                    backtrack(row+1,n,board,res)
                    board[row][col]="."
        backtrack(0,n,board,res)
        return res