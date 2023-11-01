# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        reps = set([0])
        for i in range(1,n):
            category_id = -1
            for rep in reps:
                if category_id < 0 and categoryHandler.haveSameCategory(i, rep):
                    category_id = rep
            
            if category_id < 0:
                reps.add(i)

        return len(reps)