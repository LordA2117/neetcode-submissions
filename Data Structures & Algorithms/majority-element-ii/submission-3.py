class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hashmap = {} #elem:freq
        n = len(nums)
        majority_threshold = n//3
        res = set()

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
                if hashmap[i] > majority_threshold:
                    res.add(i)
            else:
                hashmap[i] += 1
                if hashmap[i] > majority_threshold:
                    res.add(i)
        return list(res)
        