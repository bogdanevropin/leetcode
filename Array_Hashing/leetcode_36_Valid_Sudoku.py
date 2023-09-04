"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


class Solution:
	
	@staticmethod
	def isValidSudoku(board: list) -> bool:
		for n_r, row in enumerate(board):
			for n_c, num in enumerate(row):
				if num == '.':
					continue
				# check if num in row
				if row.count(num) > 1:
					return False
				# check if num in column
				if [r[n_c] for r in board].count(num) > 1:
					return False
				r_b = n_r // 3  # row 0-2
				c_b = n_c // 3  # col 0-2
				box = [r[c_b * 3: c_b * 3 + 3] for r in board[r_b * 3: r_b * 3 + 3]]
				c = 0
				for r in box:
					c += r.count(num)
				if c > 1:
					return False
		return True


if __name__ == '__main__':
	board = [["5","3",".",".","7",".",".",".","."],
	         ["6",".",".","1","9","5",".",".","."],
	         [".","9","8",".",".",".",".","6","."],
	         ["8",".",".",".","6",".",".",".","3"],
	         ["4",".",".","8",".","3",".",".","1"],
	         ["7",".",".",".","2",".",".",".","6"],
	         [".","6",".",".",".",".","2","8","."],
	         [".",".",".","4","1","9",".",".","5"],
	         [".",".",".",".","8",".",".","7","9"]]
	print(Solution.isValidSudoku(board=board))
