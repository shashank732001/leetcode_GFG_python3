class RandomizedSet:

    def __init__(self):
        self.Set = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.Set:
            self.Set.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.Set:
            self.Set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        # if self.Set:
        #     random = self.Set.pop()
        #     self.Set.add(random)
        #     return random
        # return random.sample(self.Set, 1)[0]
        return random.choice(list(self.Set))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()