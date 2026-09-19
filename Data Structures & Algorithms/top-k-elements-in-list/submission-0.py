class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict(Counter(nums))
        freq_items = sorted(list(hashmap.keys()), key=lambda x: hashmap[x], reverse=True)
        return freq_items[:k]
        