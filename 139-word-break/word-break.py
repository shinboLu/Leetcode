class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        queue = collections.deque()
        queue.append(0)
        visited = set()
        while queue:
            cur_idx = queue.popleft()
            if cur_idx == len(s):
                return True
            for i in range(cur_idx+1, len(s)+1):
                if i in visited:
                    continue
                if s[cur_idx:i] in wordDict:
                    visited.add(i)
                    queue.append(i)


        return False