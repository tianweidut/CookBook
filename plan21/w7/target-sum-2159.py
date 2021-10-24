class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target <= 2:
            return []
        
        res = []
        left, right = 1, 2
        ssum = left
        while left < (target // 2 + 1) and right < target:
            if ssum == target:
                res.append([i for i in range(left, right)])
                ssum -= left
                left += 1
            elif ssum > target:
                ssum -= left
                left += 1
            else:
                ssum += right
                right += 1
                
        return res
    
    def findContinuousSequence2(self, target: int) -> List[List[int]]:
        if target <= 2:
            return []
        
        res = []
        
        for i in range(1, target//2 + 1):
            seq = []
            ssum = 0
            for j in range(i, target):
                ssum += j
                seq.append(j)
                
                if ssum >= target:
                    break
                    
            if ssum == target and len(seq) > 1:
                res.append(seq)
        
        return res