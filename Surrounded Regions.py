__author__ = 'KH9057'
'''Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X'''
class data:
    def __init__(self):
        self.left = False
        self.right = False
        self.top = False
        self.bottom = False

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if(len(board) == 0):
            return
        List1 = []
        for i in range(0,len(board),1):
            List2 = []
            for j in range(0,len(board[i]),1):
                List2.append(data())
            List1.append(List2)
        n = len(board)
        n2 = len(board[0])
        for i in range(0,n,1):
            if(board[i][0]=='x'):
                List1[i][0].left = True
                List1[i][0].top = True
                List1[i][0].right = True
                List1[i][0].bottom = True
            n1 = n2-1
            if(board[i][n1] == 'x'):
                List1[i][n1].left = True
                List1[i][n1].right = True
                List1[i][n1].top = True
                List1[i][n1].bottom = True
        for i in range(0,n2,1):
            if(board[0][i]=='x'):
                List1[0][i].left = True
                List1[0][i].top = True
                List1[0][i].right = True
                List1[0][i].bottom = True
            if(board[n-1][i] == 'x'):
                List1[n-1][i].left = True
                List1[n-1][i].right = True
                List1[n-1][i].top = True
                List1[n-1][i].bottom = True
        for i in range(1,n,1):
            for j in range(1,n2,1):
                if(board[i][j] == 'x'):
                    List1[i][j].left = True
                    List1[i][j].top = True
                    List1[i][j].right = True
                    List1[i][j].bottom = True
                else:
                    if(List1[i][j-1]):
                        List1[i][j].left = True
                    if (List1[i-1][j]):
                        List1[i][j].top = True

        for i in range(n-2,-1,-1):
            for j in range(n2-2,-1,-1):
                if(List1[i][j+1]):
                        List1[i][j].right = True
                if (List1[i+1][j]):
                        List1[i][j].bottom = True
                if(List1[i][j].left and List1[i][j].right and List1[i][j].top and List1[i][j].bottom):
                    if(board[i][j] != 'x'):
                        board[i][j] = 'x'
        print board
sol = Solution()


sol.solve(["xxxxooo",['x','o','o','x'],['x','x','x','x']])