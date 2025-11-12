class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        # Binary search on the smaller array
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            i = (left + right) // 2 
            j = half - i             
            
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if total % 2 == 1:
                    return min(nums1_right_min, nums2_right_min)
                else:
                    return (max(nums1_left_max, nums2_left_max) + 
                            min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1
        
        return 0.0