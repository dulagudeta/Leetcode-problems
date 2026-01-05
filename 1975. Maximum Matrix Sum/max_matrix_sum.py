class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float('inf')
        negative_count = 0

        for row in matrix:
            for val in row:
                total += abs(val)
                min_abs = min(min_abs, abs(val))
                if val < 0:
                    negative_count += 1
        if negative_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs