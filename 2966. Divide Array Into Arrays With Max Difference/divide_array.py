class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        result = []
        
        # Process in groups of 3
        for i in range(0, n, 3):
            # Check if the current triplet satisfies the condition
            if nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                # If any triplet fails, return empty array
                return []
        
        return result