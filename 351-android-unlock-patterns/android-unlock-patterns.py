class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        nei = {
            2: {8: 5},
            8: {2: 5},
            4: {6: 5},
            6: {4: 5},
            1: {3: 2, 9: 5, 7: 4},
            7: {1: 4, 9: 8, 3: 5},
            3: {1: 2, 9: 6, 7: 5},
            9: {7: 8, 1: 5, 3: 6},
            5: {}
        }

        self.count = 0
        def fun(cur_val, dots, cur_dots, visited):
            if cur_dots == dots:
                self.count+=1
                return
            for i in range(1, 10):
                if i == cur_val or i in visited:
                    continue
                elif i in nei[cur_val]: 
                    if nei[cur_val][i] in visited:
                        # call the method again
                        visited.add(i)
                        fun(i, dots, cur_dots+1, visited)
                        visited.remove(i)
                    else: 
                        continue
                else:
                    visited.add(i)
                    fun(i, dots, cur_dots+1, visited)
                    visited.remove(i)
                    
        final_ans = 0
        for j in range(m, n+1):
            self.count = 0 
            fun(1, j, 1, {1})
            final_ans += self.count*4
            self.count = 0
            fun(2, j, 1, {2})
            final_ans += self.count*4
            self.count = 0 
            fun(5, j, 1, {5})
            final_ans+=self.count
        return final_ans