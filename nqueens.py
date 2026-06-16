# N-Queens Problem Using Recursion and Backtracking
N = int(input("Enter N (6 to 12): "))

# Validate input range
if N < 6 or N > 12:
    print("Invalid input! N must be between 6 and 12.")
    exit()

board = [-1] * N
solutions = 0

# Check safe position
def is_safe(row, col):

    for i in range(row):

        # Same column
        if board[i] == col:
            return False

        # Diagonal check
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

# Print board
def print_board():

    global solutions

    solutions += 1

    print(f"\nSolution {solutions}:\n")

    for i in range(N):

        for j in range(N):

            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

# Recursive function
def solve(row):

    if row == N:
        print_board()
        return

    for col in range(N):

        if is_safe(row, col):

            board[row] = col

            solve(row + 1)

            # Backtracking
            board[row] = -1

# Main Program
print(f"\nN-Queens Problem for N = {N}\n")

solve(0)

print(f"\nTotal Solutions = {solutions}")