# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.hash = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False

        self.hash[val] = len(self.arr)
        self.arr.append(val)

        return True   

    def remove(self, val: int) -> bool:
        if val not in self.arr:
            return False
        
        indx = self.hash[val]
        self.arr[indx], self.arr[-1] = self.arr[-1], self.arr[indx]

        self.hash[self.arr[indx]] = indx 

        del self.hash[val]
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()