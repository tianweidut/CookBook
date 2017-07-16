class Node(object):

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class DList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.prev = self.tail
            self.tail.next = node
            self.head.prev = node
            self.head = node

    def pop(self, node=None):
        if node is None:
            node = self.tail

        prev, next = node.prev, node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev

        if node == self.tail:
            self.tail = prev
        if node == self.head:
            self.head = next
        return node


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.dlist = DList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.dlist.pop(node)
        self.dlist.insert_head(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.dlist.pop(node)
        else:
            if len(self.cache) == self.capacity:
                node = self.dlist.pop()
                if node.key in self.cache:
                    del self.cache[node.key]

            node = Node(key, value)
            self.cache[key] = node

        self.dlist.insert_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
