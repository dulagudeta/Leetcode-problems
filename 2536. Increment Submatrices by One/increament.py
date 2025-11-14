class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Create a 2D difference array of size (n+1) x (n+1)
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        
        for r1, c1, r2, c2 in queries:
            # Mark the start of the submatrix
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        
        # Reconstruct the final matrix
        mat = [[0] * n for _ in range(n)]
        
        # First pass: accumulate row-wise
        for i in range(n):
            for j in range(n):
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]
                mat[i][j] = diff[i][j]
        
        return mat