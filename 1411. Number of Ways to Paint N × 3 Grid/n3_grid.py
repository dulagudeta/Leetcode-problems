class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        a = 6
        b = 6
        for _ in range(2, n + 1):
            new_a = (2*a + 2*b) % MOD
            new_b = (2*a + 3*b) % MOD
            a, b = new_a, new_b
    
        return (a + b) % MOD