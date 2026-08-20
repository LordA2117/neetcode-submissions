class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] += 1

        t_dict = {}
        for i in t:
            if i not in t_dict:
                t_dict[i] = 1
            else:
                t_dict[i] += 1

        print(s_dict)
        print(t_dict)
        for key in t_dict:
            if key not in s_dict:
                return False

            if s_dict[key] != t_dict[key]:
                return False
        
        for key in s_dict:
            if key not in t_dict:
                return False
            
            if s_dict[key] != t_dict[key]:
                return False

        return True
        