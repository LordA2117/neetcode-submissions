class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height)==1:
            return 0
        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)

        # Calculate prefix maximums
        prefix_max[0] = height[0]
        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i - 1], height[i])

        # Calculate suffix maximums
        suffix_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])

        total_trapped = 0
        #print(prefix_max)
        #print(suffix_max)

        for i in range(len(height)):
            total_trapped += min(prefix_max[i], suffix_max[i]) - height[i]

        return total_trapped
        