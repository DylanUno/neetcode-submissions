class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        right = 0
        longest = 0
        len_substring = 0
        left = 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            len_substring += 1

            best = max(count.values())

            if len_substring - best <= k:
                pass
            else:
                while len_substring - best > k and left < len(s):
                    count[s[left]] = count.get(s[left], 0) - 1
                    len_substring -= 1
                    left += 1
                    best = max(count.values())
            
            right += 1
            longest = max(longest, len_substring)
        
        return longest
                

            

        