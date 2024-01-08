class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_val, max_val = min(nums), max(nums) 

        bucket_size = max(1, (max_val - min_val) // (len(nums)-1)) 
        num_buckets = (max_val - min_val) // bucket_size + 1

        buckets = [None] * num_buckets

        for num in nums: 
            bucket_idx = (num - min_val) // bucket_size
            print(bucket_idx)
            if not buckets[bucket_idx]:
                buckets[bucket_idx] = {'min': num, 'max': num}
            else: 
                buckets[bucket_idx]['min'] = min(buckets[bucket_idx]['min'], num)
                buckets[bucket_idx]['max'] = max(buckets[bucket_idx]['max'], num)

        max_gap = 0
        prev_max = min_val

        for bucket in buckets:
            if bucket: 
                max_gap = max(max_gap, bucket['min'] - prev_max)
                prev_max = bucket['max']
        
        return max_gap 
        



        
        