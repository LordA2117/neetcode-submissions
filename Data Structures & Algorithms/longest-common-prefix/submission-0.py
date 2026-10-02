class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]

        i = 1
        while i < len(strs):
            curr_str = strs[i]
            check_length = min(len(curr_str), len(lcp))
            j = 0
            common_pfx = ""
            while j < check_length:
                if curr_str[j] == lcp[j]:
                    common_pfx += curr_str[j]
                else:
                    break
                j += 1
            
            if not common_pfx:
                return ""
            
            lcp = common_pfx
            i += 1
        return lcp