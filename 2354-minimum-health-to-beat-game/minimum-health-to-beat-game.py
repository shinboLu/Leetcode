class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        tot_dmg = sum(damage)
        max_dmg = max(damage)
        reduction = min(max_dmg, armor)

        return tot_dmg - reduction+1
        