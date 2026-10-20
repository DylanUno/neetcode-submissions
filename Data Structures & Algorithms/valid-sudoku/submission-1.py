class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_hash = {}
        col_hash = {}
        box_hash = {}

        row = 0
        while row < len(board):
            col = 0
            while col < len(board[row]):
                num = board[row][col]
                if num == ".":
                    col += 1
                    continue
                else:
                    box_num = (row // 3) * 3 + (col // 3)
                    if num not in row_hash:
                        row_hash[num] = [row]
                        col_hash[num] = [col]
                        box_hash[num] = [box_num]
                    else:
                        #check if it appears again in row
                        if row in row_hash[num]:
                            return False
                        else:
                            row_hash[num].append(row)
                        #check if it appears again in col
                        if col in col_hash[num]:
                            return False
                        else:
                            col_hash[num].append(col)
                        #check if it appears again in box
                        if box_num in box_hash[num]:
                            return False
                        else:
                            box_hash[num].append(box_num)
                col += 1
            row += 1
        
        return True
        