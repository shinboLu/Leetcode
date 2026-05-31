class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:

        total_dmg = sum(damage)
        if armor == 0:
            return total_dmg+1
        max_dmg = max(damage)
        
        if max_dmg < armor: 
            total_dmg -= max_dmg
        else:
            total_dmg -= armor
            
        return total_dmg+1
