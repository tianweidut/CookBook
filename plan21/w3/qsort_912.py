class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.qsort3(0, len(nums)-1, nums)
        return nums
        
    def qsort(self, i, j, nums):
        if i >= j:
            return
        
        start, end = i, j
        mid = (j - i)//2 + i
        nums[i], nums[mid] = nums[mid], nums[i]
        p = nums[i]
        
        while i < j:
            
            while i < j:
                if nums[j] >= p:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    break
                    
            while i < j:
                if nums[i] <= p:
                    i += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                    break
                    
        self.qsort(start, i-1, nums)
        self.qsort(i+1, end, nums)
        
    def qsort2(self, i, j, nums):
        if i >= j:
            return
        
        start, end = i, j
        mid = (j - i)//2 + i
        nums[i], nums[mid] = nums[mid], nums[i]
        p = nums[i]
        
        while i < j:
            while i < j and nums[j] >= p:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
                    
            while i < j and nums[i] <= p:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
                    
        self.qsort(start, i-1, nums)
        self.qsort(i+1, end, nums)
        
    def qsort3(self, i, j, nums):
        stack = []
        stack.extend([i, j])
        
        while len(stack) != 0:
            end = stack.pop()
            start = stack.pop()
            
            if start >= end:
                continue
            
            saved_end, saved_start = end, start
            mid = (end - start)//2 + start
            nums[start], nums[mid] = nums[mid], nums[start]
            
            p = nums[start]
            while start < end:
                while start < end and nums[end] >= p:
                    end -= 1
                
                nums[start], nums[end] = nums[end], nums[start]
                
                while start < end and nums[start] <= p:
                    start += 1
                
                nums[start], nums[end] = nums[end], nums[start]
                
            stack.extend([saved_start, start - 1])
            stack.extend([start + 1, saved_end])
            
                
                