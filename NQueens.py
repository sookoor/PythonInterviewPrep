class NQueens(object):
    def __init__(self, n):
        self.num_sols = 0
        self.n = n
        self.board = []
        for row in range(n):
            self.board.append([])
            for col in range(n):
                self.board[row].append(None)

    def _is_safe(self, board, row, col):
        for i in range(self.n):
            if board[row][i] or board[i][col]:
                return False
            else:
                r = row - 1
                c = col - 1
                while r >= 0 and c >=0:
                    if board[r][c]:
                        return False
                    r -= 1
                    c -= 1

                r = row + 1
                c = col - 1
        
        while r < self.n and c >= 0:
                    if board[r][c]:
                        return False
                    r += 1
                    c -= 1
        return True

    def _solve(self, board, cur_col=0):
        if cur_col == self.n:
            print(board)
            self.num_sols += 1
        else:
            for col in range(cur_col, self.n):
                for row in range(self.n):
                    if self._is_safe(board, row, col):
                        board[row][col] = 1
                        self._solve(board, cur_col + 1)
                        board[row][col] = None


    def solve(self):
        self.num_sols = 0
        self._solve(self.board)

        

if __name__ == "__main__":
    board_size = [1, 2, 3, 4, 5, 6, 7]
    num_sols   = [1, 0, 0, 2, 10, 4, 40] 

    for i in range(len(board_size)):
        n = board_size[i]
        print("Solving for " + str(n) + " queen(s)")
        n_queens = NQueens(n)
        n_queens.solve()
        assert n_queens.num_sols == num_sols[i]
