class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            hash_row = {}
            for item in row:
                if item != ".":
                    if item in hash_row:
                        print("Row fail")
                        return False
                    else:
                        hash_row[item] = 1

        # Check columns
        i = 0
        while i < 9:
            hash_col = {}
            j = 0
            while j < 9:
                item = board[j][i]
                if item != ".":
                    if item in hash_col:
                        print("col fail")
                        return False
                    else:
                        hash_col[item] = 1
                j += 1
            i += 1

        # Check square
        hash_square = {}
        for i in range(9):
            hash_square[i] = []
        for row_idx in range(len(board)):
            row = board[row_idx]
            for col_idx in range(len(row)):
                sq_idx = ((row_idx // 3) * 3) + (col_idx // 3)
                item = board[row_idx][col_idx]
                if item != ".":
                    if item in hash_square[sq_idx]:
                        print("Square fail")
                        return False
                    else:
                        hash_square[sq_idx].append(item)
        return True
        