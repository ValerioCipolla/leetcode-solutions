class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i, b in enumerate(boxes):
            moves = 0
            for i2, b2 in enumerate(boxes):
                if i == i2: continue
                if b2 == "1":
                    moves += abs(i2 - i)
            res.append(moves)
        return res
            