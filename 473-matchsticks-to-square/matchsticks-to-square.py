class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot = sum(matchsticks)
        if tot % 4 != 0:
            return False

        req_len = tot // 4 
        
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def backtracking_return_boolean(start_index):
            if start_index == len(matchsticks):
                return True
            
            for i in range(4):
                if sides[i] + matchsticks[start_index] <= req_len:
                    sides[i] += matchsticks[start_index]

                    if backtracking_return_boolean(start_index + 1):
                        return True
                    
                    sides[i] -= matchsticks[start_index]

                    if sides[i] == 0:
                        break

            return False

        return backtracking_return_boolean(0)


            

                
