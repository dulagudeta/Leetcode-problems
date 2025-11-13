MOD = 10**9 + 7

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        r = n - k  # number of runs
        
        # Edge cases
        if r < 1 or r > n:
            return 0
        if m == 1:
            return 1 if k == n - 1 else 0
        
        # Compute combination C(n-1, r-1) using multiplicative formula
        def nCr(n_val, r_val):
            if r_val < 0 or r_val > n_val:
                return 0
            r_val = min(r_val, n_val - r_val)
            res = 1
            for i in range(r_val):
                res = res * (n_val - i) % MOD
                res = res * pow(i + 1, MOD - 2, MOD) % MOD
            return res
        
        ways_to_split = nCr(n - 1, r - 1)
        ways_to_assign = m * pow(m - 1, r - 1, MOD) % MOD
        
        return ways_to_split * ways_to_assign % MOD