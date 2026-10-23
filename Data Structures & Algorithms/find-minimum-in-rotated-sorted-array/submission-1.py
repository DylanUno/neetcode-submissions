class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        low = 0

        while low < right:
            mid = (low + right) // 2

            if nums[mid] > nums[right]:
                low = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            
        return nums[right]




        