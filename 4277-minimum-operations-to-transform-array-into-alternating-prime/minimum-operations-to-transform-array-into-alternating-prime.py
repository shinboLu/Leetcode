class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def check_is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True 

        res = 0 
        for idx, val in enumerate(nums):
            if idx % 2 == 0:
                while not check_is_prime(val):
                    val+=1
                    res+=1
            else:
                while check_is_prime(val):
                    val += 1
                    res += 1

        return res
