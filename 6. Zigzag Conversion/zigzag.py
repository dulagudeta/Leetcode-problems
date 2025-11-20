class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = []
        cycle_len = 2 * numRows - 2
        
        for row in range(numRows):
            i = row
            while i < len(s):
                result.append(s[i])
                
                if row != 0 and row != numRows - 1:
                    diagonal_index = i + cycle_len - 2 * row
                    if diagonal_index < len(s):
                        result.append(s[diagonal_index])
                
                i += cycle_len
        
        return ''.join(result)