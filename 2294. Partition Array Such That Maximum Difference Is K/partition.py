class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        current_min = nums[0]
        
        for num in nums:
            # If adding this number would make the range > k, start new subsequence
            if num - current_min > k:
                count += 1
                current_min = num
        
        return count