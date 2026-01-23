class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_dmg = max(damage)
        max_hp = sum(damage)
        reduction = min(max_dmg, armor)
        return max_hp - reduction+1

