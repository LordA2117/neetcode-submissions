class TimeMap:

    def __init__(self):
        self.dictionary = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dictionary:
            self.dictionary[key] = [(value, timestamp)]
        else:
            self.dictionary[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
        items = self.dictionary[key]
        left = 0
        right = len(items)-1
        while left <= right:
            mid = left + (right - left)//2
            v,t = items[mid]
            if t > timestamp:
                right = mid -1
            else:
                left = mid + 1
        if right >= 0:
            return items[right][0]
        else:
            return ""

        
