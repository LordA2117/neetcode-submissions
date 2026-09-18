class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i != j:
            test_sum = numbers[i]+numbers[j]
            if test_sum > target:
                j -= 1
            
            if test_sum < target:
                i += 1
            
            if test_sum == target:
                return [i+1, j+1]
        