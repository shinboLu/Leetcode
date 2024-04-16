class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def transform(x):
            # Return the transformed result for element 'x'
            return (a * x * x) + (b * x) + c

        res = [] 
        left = 0
        right = len(nums)-1

        if a < 0:
            while left <= right:
                left_val = transform(nums[left])
                right_val = transform(nums[right])

                if left_val < right_val:
                    res.append(left_val)
                    left += 1
                else:
                    res.append(right_val)
                    right-=1 
        else:
            while left <= right:
                left_val = transform(nums[left])
                right_val = transform(nums[right])
                if left_val > right_val:
                    res.append(left_val)
                    left += 1
                else:
                    res.append(right_val)
                    right -= 1
            res.reverse() 

        return res 

