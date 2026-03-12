class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        def get_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True
        
        valid_primes = [x for x in range(n+1) if get_prime(x)][:m]
        queue = collections.deque()
        queue.append([0,0])
        visited = set([0])
        while queue:
            cur_sum, cur_count = queue.popleft()
            if cur_sum == n:
                return cur_count
            
            for prime in valid_primes:
                nxt_sum = cur_sum + prime
                if nxt_sum <= n and nxt_sum not in visited:
                    visited.add(nxt_sum)
                    queue.append([nxt_sum, cur_count+1])
        
        return -1


