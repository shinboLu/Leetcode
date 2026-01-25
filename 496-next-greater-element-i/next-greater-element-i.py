class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i, num1 in enumerate(nums1):
            found = False
            target = -1 
            for j, num2 in enumerate(nums2):
                if not found:
                    if num1 == num2:
                        found = True
                else:
                    if num2 > num1:
                        target = num2
                        break
            res.append(target)

        return res



            

                

                    
