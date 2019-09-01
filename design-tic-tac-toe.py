class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.vertical = {i: [0] * 2 for i in range(n)}
        self.horizonal = {i: [0] * 2 for i in range(n)}
        self.diagonal1 = [0] * 2
        self.diagonal2 = [0] * 2
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        res = 0
        currP = player - 1
        oppoP = 3 - player - 1
        
        # update diagonal1
        if row == col:
            self.diagonal1[currP] += 1
        if self.diagonal1[currP] == self.n:
            res = player
        
        # update diagonal2
        if row + col == self.n - 1:
            self.diagonal2[currP] += 1
        if self.diagonal2[currP] == self.n:
            res = player
        
        # update vertical lines
        self.vertical[col][currP] += 1
        if self.vertical[col][currP] == self.n:
            res = player
        
        # update horizontal lines
        self.horizonal[row][currP] += 1
        if self.horizonal[row][currP] == self.n:
            res = player
        
        return res


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
