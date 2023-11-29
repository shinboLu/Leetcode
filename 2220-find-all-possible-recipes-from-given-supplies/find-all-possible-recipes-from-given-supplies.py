from collections import deque, defaultdict, Counter

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph, in_degree = defaultdict(set), Counter()
        for recipe, ingredient in zip(recipes, ingredients):
            for item in ingredient:
                graph[item].add(recipe)
            in_degree[recipe] = len(ingredient)

        
        available, res = deque(supplies), []

        while available:
            supply = available.popleft()
            for recipe in graph[supply]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    available.append(recipe)
                    res.append(recipe)

        return res 
        

        