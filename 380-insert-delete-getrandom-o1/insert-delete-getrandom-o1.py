class RandomizedSet:

    def __init__(self):
        self.values = {} # val -> index
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.values[val] = len(self.arr)
        self.arr.append(val)
        #print(f'add {self.arr} {self.values}')
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        index = self.values[val]
        self.values[self.arr[-1]] = index
        self.values.pop(val)

        #swap
        temp = self.arr[index]
        self.arr[index] = self.arr[-1]
        self.arr[-1] = temp
        self.arr.pop()
        #print(f'remove {self.arr} {self.values}')
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()