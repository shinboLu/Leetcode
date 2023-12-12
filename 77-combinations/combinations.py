class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def find_unique_combination(index, path):
            if index == n:
                if len(path) == k:
                    res.append(path.copy())
                    return

            if len(path) == k:
                res.append(path.copy())
                return

            for i in range(index, n+1):
                path.append(i)
                find_unique_combination(i+1, path)
                path.pop()

        find_unique_combination(1, [])
        return res 

            