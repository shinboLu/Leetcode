class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_map = collections.defaultdict(int)
        prefix_map[0] =1
        cur_odd_count = 0
        res = 0
        for num in nums:
            if num %2 ==1:
                cur_odd_count +=1
            
            res += prefix_map[cur_odd_count-k]
            prefix_map[cur_odd_count] +=1

        return res
