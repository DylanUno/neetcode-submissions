class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}

        for i in t:
            hash_t[i] = hash_t.get(i, 0) + 1
        
        need = len(hash_t)
        
        left = 0
        right = 0
        find = {}
        have = 0

        substrings = {}

        while right < len(s):
            if s[right] in hash_t:
                find[s[right]] = find.get(s[right], 0) + 1
            
                if find[s[right]] == hash_t[s[right]]:
                    have += 1
            
            while have == need:
                substrings[(left, right)] = right - left

                if s[left] in hash_t:
                    find[s[left]] -= 1
                    if find[s[left]] < hash_t[s[left]]:
                        have -= 1
                left += 1

            right += 1

        if not substrings:
            return ""

        smallest = min(substrings, key=substrings.get)
        output_l, output_r = smallest
        output = s[output_l:output_r + 1]
        return output