from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        hq = []
        for task, counts in counter.items():
            heappush(hq, [-counts, task])
        time = 0
        while hq:
            temp = []
            cycle = 0
            for i in range(n+1): 
                if hq:
                    cnt, task = heappop(hq)
                    cnt+=1
                    cycle+=1
                    if cnt < 0:
                        temp.append([cnt, task])
                else:
                    break
            for item in temp:
                heappush(hq, item)

            
            if hq:
                time += n+1
            else:
                time+= cycle
        return time

