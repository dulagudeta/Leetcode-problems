class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        ones_count = 0
        zeros_after_last_one = 0
        
        for char in s:
            if char == '0':
                if ones_count > 0:
                    # These zeros can be used by all preceding ones
                    operations += ones_count
            else:  # char == '1'
                ones_count += 1
        
        return operations