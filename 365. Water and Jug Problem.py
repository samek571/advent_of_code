class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        return targetCapacity <= jug2Capacity+jug1Capacity and not targetCapacity%math.gcd(jug1Capacity,jug2Capacity)
