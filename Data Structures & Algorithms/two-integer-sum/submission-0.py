class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target-x
            if y in dictionary:
                return sorted([i, dictionary[y]])
            else:
                dictionary[x] = i
    
        