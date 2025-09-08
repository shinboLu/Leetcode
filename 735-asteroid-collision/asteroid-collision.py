class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = [] 

        for a in asteroids:
            alive = True
            while res and a < 0 < res[-1]:
                if abs(a) > res[-1]:
                    res.pop()
                    continue
                elif abs(a) == abs(res[-1]):
                    res.pop()
                alive = False
                break
            if alive:
                res.append(a)

        return res