from heapq import heapify, heappop, heappush
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort(reverse=True)  
        print(nums1)
        nums1_p = 0
        res = 0

        heapify(nums2) 

        while nums2:
            nums2_pop = heappop(nums2)
            res += (nums2_pop * nums1[nums1_p])
            nums1_p+=1

        return res
