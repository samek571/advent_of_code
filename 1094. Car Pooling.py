class Solution:
    def carPooling(trips, capacity) -> bool:
        cars = [0]*1001 #cuz of trip lenght

        for i in trips:
            cars[i[1]]+=i[0]
            cars[i[2]]-=i[0]

        for i in cars:
            capacity -= i
            if capacity<0: return False

        return True
