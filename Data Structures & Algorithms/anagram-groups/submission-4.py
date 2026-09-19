class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            if tuple(sorted(string)) not in hashmap:
                hashmap[tuple(sorted(string))] = [string]
            else:
                hashmap[tuple(sorted(string))].append(string)

        return list(hashmap.values())
        