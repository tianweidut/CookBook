
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.keys = defaultdict(list)
        self.vals = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag = val not in self.keys

        index = len(self.vals) + 1
        self.vals[index] = val
        self.keys[val].append(index)
        return flag

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.keys:
            return False

        index = self.keys[val].pop()
        if len(self.keys[val]) == 0:
            del self.keys[val]

        size_vals = len(self.vals)
        if index == size_vals:
            del self.vals[index]
        else:
            last = self.vals[size_vals]
            self.vals[index] = last
            del self.vals[size_vals]
            self.keys[last].remove(size_vals)
            self.keys[last].append(index)

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return self.vals[random.randint(1, len(self.vals))]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
