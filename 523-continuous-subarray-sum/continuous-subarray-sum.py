class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_mod = 0 
        mapping = {0:-1}

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) %k
            if prefix_mod in mapping:
                if i - mapping[prefix_mod] > 1:
                    return True
            else:
                mapping[prefix_mod] = i
        return False