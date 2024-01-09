class Solution:
    # T = O(Nlog(K)) for the heap popping happening n times 
    # S = O(K) for the heap
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ans = -math.inf, math.inf # max range to start with

        heap = []
        
        high = -math.inf
        # track max out of first starting list of numbers 
        # and also add them to min heap
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            high = max(high, nums[i][0])
        #print(heap)
        while True:
            low, id, ind = heapq.heappop(heap)

            if high - low < ans[1] - ans[0]:
                ans = (low, high)

            if ind + 1 == len(nums[id]):
                return ans

            next = nums[id][ind+1]

            # find new max
            high = max(high, next)

            heapq.heappush(heap, (next, id, ind+1))