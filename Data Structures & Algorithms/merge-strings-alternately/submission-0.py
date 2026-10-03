class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = [""] * (len(word1) + len(word2))

        if len(word1) <= len(word2):
            # Add word1 to the right positions
            i = 0
            ctr = 0
            while ctr < len(word1):
                res[i] = word1[ctr]
                i += 2
                ctr += 1
            
            # Fill the remaining spots with word2
            ctr = 0
            for i in range(len(res)):
                if not res[i]:
                    res[i] = word2[ctr]
                    ctr += 1
        else:
            # Add word2 to all the right positions
            i = 1
            ctr = 0
            while ctr < len(word2):
                res[i] = word2[ctr]
                i += 2
                ctr += 1

            # Fill the remaining spots with word1
            ctr = 0
            for i in range(len(res)):
                if not res[i]:
                    res[i] = word1[ctr]
                    ctr += 1
        return "".join(res)