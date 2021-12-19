
class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        return self.construct(A) == self.construct(B)
        
    def construct(self, strings):
        from collections import defaultdict
        hash_s = defaultdict(int)
        for s in strings:
            hash_s[s] += 1
            
        return hash_s
