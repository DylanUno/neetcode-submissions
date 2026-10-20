class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
             # positive is impossible, in ascending list
            if nums[i] > 0:
                break
            
            j, k = i + 1, n - 1
            target = -nums[i]

            while j < k:
                current_sum = nums[j] + nums[k]

                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return res
            




        