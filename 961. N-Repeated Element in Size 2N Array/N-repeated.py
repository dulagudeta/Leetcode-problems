class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        
        while True:
            i = random.randrange(n)
            j = random.randrange(n)
                
            if i != j and nums[i] == nums[j]:
                return nums[i]