class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(x):
                if x < 2:
                    return False
                for i in range(2, int(x ** 0.5) + 1):
                    if x % i == 0:
                        return False
                return True

        total = 0

        for n in nums:
            p = round(n ** (1/3))
            if p ** 3 == n and is_prime(p):
                total += 1 + p + p*p + n
                continue

            for d in range(2, int(n ** 0.5) + 1):
                if n % d == 0:
                    other = n // d
                    if d != other and is_prime(d) and is_prime(other):
                        total += 1 + d + other + n
                    break

        return total