class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        past = {}
        low = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in past:
                low = max(low,past[s[right]] + 1)

            max_length = max(max_length, right-low+1)
            past[s[right]] = right
        return max_length
            
                



        