class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        state = {}  # will contain each character and its frequency in the substring

        for i in s:
            state[i] = 0

        max_ = 0
        n = len(s)

        for end in range(n):
            char = s[end]

            state[char] += 1

            while state[char] > 1:
                state[s[start]] -= 1
                start += 1

            max_ = max(max_, end - start + 1)

        return max_
        