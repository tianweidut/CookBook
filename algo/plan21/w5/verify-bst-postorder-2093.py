class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if postorder is None or len(postorder) == 0:
            return True
        
        root_val = postorder[-1]
        larger_idx = -1
        
        for idx, val in enumerate(postorder[:-1]):
            if val > root_val:
                larger_idx = idx
                break
                
        
        for val in postorder[larger_idx:-1]:
            if val < root_val:
                return False
            
        return self.verifyPostorder(postorder[:larger_idx]) and self.verifyPostorder(postorder[larger_idx:-1])