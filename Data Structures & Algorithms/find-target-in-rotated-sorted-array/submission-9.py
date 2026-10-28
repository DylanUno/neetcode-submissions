class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0

        if right == left:
            if nums[0] == target:
                return 0
            else:
                return -1

        while left < right:

            if right - left == 1:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                else:
                    return -1

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] > nums[right]:
                if target > nums[right] and target < nums[mid]:
                    right = mid

                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid

        if nums[left] == target:
            return left
        
        return -1
            
        