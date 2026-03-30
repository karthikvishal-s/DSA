def solve(board):
    m, n = len(board), len(board[0])

    def find_neigh(r, c):
        count = 0
        for i in range(max(0, r-1), min(m, r+2)):
            for j in range(max(0, c-1), min(n, c+2)):
                if i == r and j == c: continue
                # We check for 1 or 3 because those were "originally alive"
                if board[i][j] in [1, 3]:
                    count += 1
        return count

    for i in range(m):
        for j in range(n):
            count = find_neigh(i, j)
            
            # Rule 1 & 3: Alive cell
            if board[i][j] == 1:
                if count == 2 or count == 3:
                    board[i][j] = 3 # Stays alive
                # Else stays 1 (meaning it will die)
            
            # Rule 4: Dead cell
            elif board[i][j] == 0:
                if count == 3:
                    board[i][j] = 2 # Becomes alive

    # Final pass: Convert 2 and 3 to 1, and 1 to 0
    for i in range(m):
        for j in range(n):
            if board[i][j] in [2, 3]:
                board[i][j] = 1
            else:
                board[i][j] = 0

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
solve(board)
print(board)