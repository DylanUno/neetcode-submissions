class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        i = 0
        while i < len(nums):
            j = 0
            while j < len(result):
                if i == j:
                    j+=1
                    continue
                result[j] *= nums[i]
                j+=1
            i+=1
        
        return result
        