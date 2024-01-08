class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if not nums or valueDiff < 0:
            return False

        min_val = min(nums)
        # A lambda function generate buckey key given a value
        bucket_key = lambda x: (x-min_val) // (valueDiff +1)
        
        d = collections.defaultdict(lambda: float('inf'))

        for i, num in enumerate(nums):
            num_bucket_key = bucket_key(num)
            for nei in [d[num_bucket_key-1], d[num_bucket_key], d[num_bucket_key+1]]:
                if abs(nei - num) <= valueDiff:
                    return True
            d[num_bucket_key] = num
            if i >= indexDiff:
                d.pop(bucket_key(nums[i-indexDiff]))
        return False



