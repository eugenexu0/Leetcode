class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hashmap.get(key):
            self.hashmap[key].append([timestamp, value])
        else:
            self.hashmap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if self.hashmap.get(key):
            index = bisect.bisect_right(self.hashmap[key], timestamp, key=lambda x:x[0]) - 1
            if index >= 0:
                return self.hashmap[key][index][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)