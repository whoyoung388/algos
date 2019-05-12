import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.positions = {}
        self.items = []
        self.size = 0


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.positions:
            return False
        
        self.positions[val] = self.size
        self.size += 1
        self.items.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.positions:
            return False
        
        loc = self.positions[val]
        last = self.items[-1]
        self.items[loc], self.items[-1] = self.items[-1], self.items[loc]
        
        self.items.pop()
        self.size -= 1
        self.positions[last] = loc
        del self.positions[val]
        
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.items)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
