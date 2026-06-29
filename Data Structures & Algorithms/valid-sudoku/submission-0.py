class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        boxes={}
        for i in range(len(board)):
            rows[i] = []
            columns[i] = []
            boxes[i]=[]

        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                if row[j]!=".":
                    b = (i // 3) * 3 + (j // 3)
                    if row[j] in columns[j]:
                        return False
                    columns[j].append(row[j])
                    if row[j] in rows[i]:
                        return False
                    rows[i].append(row[j])
                    if row[j] in boxes[b]:
                        return False
                    boxes[b].append(row[j])
        print(rows)
        print(columns)
        return True
                    