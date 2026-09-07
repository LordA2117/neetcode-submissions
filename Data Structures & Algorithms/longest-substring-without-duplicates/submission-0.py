class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_ = 0
        state = {}
        n = len(s)

        for end in range(n):
            char = s[end]

            if char in state and state[char] >= start:
                start = state[char] + 1
            
            state[char] = end

            max_ = max(max_, end - start + 1)
        
        return max_
        