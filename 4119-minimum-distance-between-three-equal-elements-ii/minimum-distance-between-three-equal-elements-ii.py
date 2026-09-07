class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mapping = collections.defaultdict(list)
        res = float('inf')
        for idx, val in enumerate(nums):
            mapping[val].append(idx)

        for num_val, idices in mapping.items():
            if len(idices) < 3:
                continue
            for i in range(len(idices)-2):
                p1, p2, p3 = idices[i], idices[i+1], idices[i+2]
                res = min(res, abs(p1-p2)+abs(p2-p3)+abs(p3-p1))
        
        return res if res!= float('inf') else -1