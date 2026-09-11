class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        state = {}
        max_ = 0

        for i in s:
            state[i] = 0

        for end in range(len(s)):
            char = s[end]

            state[char] += 1

            most_freq_char = max(state.values())
            num_replacements = (end - start + 1) - most_freq_char

            while num_replacements > k and start < end:
                state[s[start]] -= 1
                start += 1
                most_freq_char = max(state.values())
                num_replacements = (end - start + 1) - most_freq_char
            
            max_ = max(max_, end-start+1)
        return max_