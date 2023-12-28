from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapify(maxHeap)
        queue = collections.deque()
        time = 0

        while maxHeap or queue:
            time += 1
            if maxHeap:
                cur_cnt = 1 + heappop(maxHeap)

                if cur_cnt:
                    queue.append([cur_cnt, time+n])
            if queue and queue[0][1] == time: #check the idle time
                heappush(maxHeap, queue.popleft()[0])

        return time 