class KnightTour:
    def __init__(self, N, startX, startY):
        self.N = N
        self.board = [[-1 for _ in range(N)] for _ in range(N)]
        self.moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        self.startX, self.startY = startX, startY

    def is_valid_move(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.board[x][y] == -1

    def knight_tour(self):
        stack = [(self.startX, self.startY, 0)]
        self.board[self.startX][self.startY] = 0

        while stack:
            x, y, move_count = stack[-1]

            if move_count == self.N * self.N - 1:
                return True


            for dx, dy in self.moves:
                next_x, next_y = x + dx, y + dy
                if self.is_valid_move(next_x, next_y):
                    self.board[next_x][next_y] = move_count + 1
                    stack.append((next_x, next_y, move_count + 1))
                    break
            else:
                self.board[x][y] = -1
                stack.pop()

        return False

#test
N = int(input("輸入棋盤大小 N: "))
startX, startY = map(int, input("輸入起始位置 (startX, startY): ").split())

knight_tour = KnightTour(N, startX, startY)
result = knight_tour.knight_tour()
print(result)
