# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        res = [0]

        for i in range(1, n): ## loop in nodes
            exist = False

            for j in res:
                if categoryHandler.haveSameCategory(i, j):
                    exist = True
                    break
            if not exist: 
                res.append(i)
        return len(res)