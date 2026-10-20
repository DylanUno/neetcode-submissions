class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = {}

        if len(nums) == 0:
            return 0

        for i in nums:
            if i in hash:
                continue
            else:
                hash[i] = True
        
        longest = 1
        for i in nums:
            temp_longest = 0
            if i-1 not in hash:
                temp_longest += 1
                while(i + temp_longest in hash):
                    temp_longest += 1
            
            if longest < temp_longest:
                longest = temp_longest
        
        return longest


        