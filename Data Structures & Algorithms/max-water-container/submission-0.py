class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_water = 0

        while i < j:

            temp_max_water = (j - i) * min(heights[i], heights[j])

            if max_water < temp_max_water:
                max_water = temp_max_water
            
            if heights[i] <= heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
        
        return max_water
        