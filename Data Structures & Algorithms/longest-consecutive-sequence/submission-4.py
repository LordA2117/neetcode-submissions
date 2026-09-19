class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # For any i in array check if i-1 is there, if not, it is the start of a sequence. Iterate until you cant get more, store this element, plus the sequence length in the hashmap. then return the max value
        hashmap = {}  # seq_start:length_of_seq
        nums = set(nums)
        for i in nums:
            if i in hashmap:
                continue
            if i - 1 not in nums:
                hashmap[i] = 1
                next_present = True
                start = i
                while next_present:
                    start += 1
                    if start not in nums:
                        next_present = False
                    else:
                        hashmap[i] += 1
        if not hashmap:
            return 0
        else:
            return max(hashmap.values())
            