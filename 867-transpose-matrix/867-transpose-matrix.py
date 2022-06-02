class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        pos = 0
        while pos < len(matrix[0]):
            res.append([])
            for i in range(len(matrix)):
                res[pos].append(matrix[i][pos])
            pos += 1
        return res