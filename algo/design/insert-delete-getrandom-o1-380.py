
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_map = {}
        self.value_map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.key_map:
            return False

        index = len(self.value_map) + 1
        self.key_map[val] = index
        self.value_map[index] = val
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.key_map:
            return False

        index = self.key_map[val]
        del self.key_map[val]

        last = len(self.value_map)
        if index == last:
            del self.value_map[index]
        else:
            val = self.value_map[last]
            self.value_map[index] = val
            self.key_map[val] = index
            del self.value_map[last]

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        rindex = random.randint(1, len(self.value_map))
        return self.value_map[rindex]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
