class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        cur = 0 

        stack = [] 

        for ast in asteroids:
            if ast >= 0:
                stack.append(ast) 
            else:
                cur = ast
                while stack and stack[-1] > 0 and cur < 0:
                    if abs(cur) == stack[-1]:
                        stack.pop()
                        cur = 0 
                        break
                    elif abs(cur) > stack[-1]:
                        stack.pop()
                    else: 
                        cur = 0
                if cur < 0:
                    stack.append(cur)
        return stack