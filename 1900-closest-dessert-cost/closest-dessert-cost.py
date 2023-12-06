class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.cost = baseCosts[0]
        # my trick here: double the toppings list since each topping can only be used at most twice -- so I don't need to care about this restriction down the road
        toppings = toppingCosts + toppingCosts

        # toppingIdx: point to current topping
        # used: cost of picked items (base + topping)
        @lru_cache(None)
        def dfs(toppingIdx, used):
            # base case
            if used > target:
                # update if closer
                if used - target < abs(self.cost - target):
                    self.cost = used
                # end here since used is already exceed target
                return
            # update if closer
            if target - used <= abs(self.cost - target):
                self.cost = used
            # reach end of the topping list
            if toppingIdx == len(toppings):
                return
            
            # move onto next
            # pick current item
            dfs(toppingIdx+1, used+toppings[toppingIdx])
            # skip current item
            dfs(toppingIdx+1, used)

        # try out different base
        for base in baseCosts:
            dfs(0, base)
            
        return self.cost