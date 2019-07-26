class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bank = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.bank:
            self.bank[number] += 1
            return
        self.bank[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.bank:
            if value - num not in self.bank:
                continue

            self.bank[num] -= 1
            if self.bank[value - num] > 0:
                self.bank[num] += 1
                return True
            self.bank[num] += 1
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
