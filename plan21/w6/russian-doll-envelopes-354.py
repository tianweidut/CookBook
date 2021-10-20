class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        from operator import itemgetter
        envelopes = sorted(envelopes, key=itemgetter(1), reverse=True)
        envelopes = sorted(envelopes, key=itemgetter(0))
        
        res = [1] * len(envelopes)
        
        for i in range (1, len(envelopes)):
            res[i] = max([res[j] + 1 for j in range(0, i) if envelopes[j][1] < envelopes[i][1]] or [1])
        
        return max(res)