class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows

        for row in board:
            s = set()
            for item in row:
                if item == '.':
                    continue
                if item in s:
                    return False
                s.add(item)

        # validate columns
        for i in range(9):
            s = set()
            for row in board:
                item = row[i]
                if item == '.':
                    continue
                if item in s:
                    return False
                s.add(item)

        # validate 3x3
        for x in range(3):
            for y in range(3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        item = board[3*x + i][3*y + j]
                        if item == '.':
                            continue
                        if item in s:
                            return False
                        s.add(item)


        return True
        