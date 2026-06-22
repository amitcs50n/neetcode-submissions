class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for num in board:
            seen = set()

            for i in num:
                if i.isdigit() and 1 <= int(i) <= 9:
                    if i in seen:
                        return False

                    seen.add(i)

        # Check columns
        for col in range(len(board[0])):
            seen = set()

            for row in range(len(board)):
                cell = board[row][col]

                if cell.isdigit() and 1 <= int(cell) <= 9:
                    if cell in seen:
                        return False

                    seen.add(cell)

        # Check 3x3 boxes
        for box_row in range(0, len(board), 3):
            for box_col in range(0, len(board[0]), 3):
                seen = set()

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        cell = board[row][col]

                        if cell.isdigit() and 1 <= int(cell) <= 9:
                            if cell in seen:
                                return False

                            seen.add(cell)

        return True