class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.dic = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.data.append(number)
        self.dic[number] = len(self.data) - 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in range(len(self.data)):
            tar = value - self.data[i]
            if tar in self.dic and self.dic[tar] != i:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)