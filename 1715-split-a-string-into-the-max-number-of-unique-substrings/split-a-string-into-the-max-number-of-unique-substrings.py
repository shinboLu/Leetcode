class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtracking_return_max_number(start, visited):
            if start == len(s):
                return len(visited)

            curr = ''
            unique_number = 0

            for i in range(start, len(s)):
                curr += s[i]

                if curr in visited:
                    continue
                
                visited.add(curr)
                unique_number = max(unique_number, backtracking_return_max_number(i+1, visited))
                visited.remove(curr)

            return unique_number

        return backtracking_return_max_number(0, set())
         


            

            
