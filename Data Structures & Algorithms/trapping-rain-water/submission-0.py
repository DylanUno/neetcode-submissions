class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0

        if n == 0:
            return total
        
        prefix = [0] * n
        suffix = [0] * n

        for i in range(n):
            prefix[i] = max(prefix[i-1], height[i])
        
        suffix[n - 1] = height[n - 1]
        for j in range(n - 2, -1, -1):
            suffix[j] = max(suffix[j + 1], height[j])

        for k in range(n):
            total += min(prefix[k], suffix[k]) - height[k]

        return total