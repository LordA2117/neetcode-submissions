class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_state = {}
        for i in s1:
            if i not in s1_state:
                s1_state[i] = 1
            else:
                s1_state[i] += 1
        
        state = {}
        start = 0

        for end in range(len(s2)):
            char = s2[end]
            if char not in state:
                state[char] = 1
            else:
                state[char] += 1
            
            if end-start+1 == len(s1):
                if state == s1_state:
                    return True
                
                state[s2[start]] -= 1
                if state[s2[start]] == 0:
                    del state[s2[start]]
                start += 1
        return False
        