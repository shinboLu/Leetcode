class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n
        
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0

        for i,n in self.nonzeros.items():
            if i in vec.nonzeros:
                res += n * vec.nonzeros[i]
        return res 
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)