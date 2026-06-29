class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_cols = [set() for _ in range(9)]
        valid_boxes = [set() for _ in range(9)]

        for row in range(len(board)):
            valid_row = set()
            for col in range(len(board[row])):
                val = board[row][col]
                if val == ".":
                    continue
                box = (row // 3) * 3 + (col // 3)
                if val in valid_row or val in valid_cols[col] or val in valid_boxes[box]:
                    return False
                
                valid_row.add(val)
                valid_cols[col].add(val)
                valid_boxes[box].add(val)

        return True