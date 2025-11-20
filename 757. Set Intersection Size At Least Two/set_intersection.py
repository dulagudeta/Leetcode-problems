class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end point
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        result = 0
        largest = -1
        second_largest = -1
        
        for start, end in intervals:
            if start <= second_largest:
                continue
            elif start <= largest:
                second_largest = largest
                largest = end
                result += 1
            else:
                largest = end
                second_largest = end - 1
                result += 2
        
        return result