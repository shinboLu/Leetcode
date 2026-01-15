class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        area = []
        start_idx = float('inf')
        end_idx = float('-inf')
        for start, end in lights:
            area.append([start-end, start+end])
        mapping = collections.defaultdict(int)
        for start, end in area: 
            mapping[start] += 1
            mapping[end+1] -=1
        
        cur, max_idx, max_val = 0, -1, float('-inf')
        for idx, val in sorted(mapping.items()):
            cur+=val
            if cur > max_val:
                max_val, max_idx = cur, idx
        return max_idx





