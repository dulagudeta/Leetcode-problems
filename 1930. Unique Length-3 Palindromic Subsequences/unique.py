class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [float('inf')] * 26
        last = [float('-inf')] * 26
        
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = max(last[idx], i)
        
        result = 0
        
        for outer in range(26):
            if first[outer] == float('inf'):
                continue
                
            for middle in range(26):
                found = False
                for pos in range(first[outer] + 1, last[outer]):
                    if ord(s[pos]) - ord('a') == middle:
                        found = True
                        break
                if found:
                    result += 1
        
        return result