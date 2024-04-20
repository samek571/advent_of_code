class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        x, y = sum(damage), max(damage)
        return 1+x-y if armor>=y else 1+x-armor
