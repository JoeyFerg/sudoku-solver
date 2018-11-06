import sys
import time


# Read the file and populate the matrix with the correct numbers
def read_file(file):
	f = open(file, 'r')

	# Set initial 9 x 9 matrix to all 0's
	matrix = [[0 for x in range(9)] for y in range(9)]

	i = 0
	while True:
		j = 0
		char = f.readline()
		for c in char:
			# Populate the matrix with the starting numbers from the file
			matrix[i][j] = int(c)
			j = j + 1
			if j == 9:
				i = i + 1
				break
		if i == 9:
			break
	return matrix


# Helper function that checks to see if the result is a sudoku
def check_sudoku(row, col, number, board):
	check = 0
	for i in range(0, 9):
		if board[row][i] == number:
			check = 1
	for i in range(0, 9):
		if board[i][col] == number:
			check = 1
	row = row - row % 3
	col = col - col % 3

	for i in range(0, 3):
		for j in range(0, 3):
			if board[row+i][col+j] == number:
				check = 1
	if check == 1:
		return False
	else:
		return True


# Recursive function that iterates through to figure out missing numbers
def sudoku_solver(matrix):
	row = 0
	col = 0
	zeros_remaining = False
	for i in range(0, 9):
		for j in range(0, 9):
			if matrix[i][j] == 0:
				zeros_remaining = True
				row = i
				col = j
				break

	# If all the spots on the matrix have been filled, the solution has been found
	if zeros_remaining is False:
		print("Solution: ")
		for i in matrix:
			print(i)
		return

	# Recursion
	for i in range(0, 10):
		if check_sudoku(row, col, i, matrix):
			matrix[row][col] = i
			if sudoku_solver(matrix):
				return True
			matrix[row][col] = 0
	return False


# Time the solver
def solve():
	start = time.time()
	sudoku_solver(grid)
	end = time.time()
	elapsed = end - start
	elapsed = round(elapsed, 2)
	print("Elapsed: " + str(elapsed) + " seconds")


grid = read_file(sys.argv[1])
solve()
