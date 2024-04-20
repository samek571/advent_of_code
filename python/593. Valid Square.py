# class Solution:
#     def validSquare(self,p1, p2, p3, p4) -> bool:
#         """
# 
#         1/3q and 2/4q musi byt slope 1 and -1 respectively
#         1/2q and 3/4q xaxis = 1
#         3/2q and 1/4q yaxis = 1
#         """
# 
#         #6 because four square vertecies can be connected 6ways
#         d12 = self.distance(p1, p2)
#         d13 = self.distance(p1, p3)
#         d14 = self.distance(p1, p4)
#         d23 = self.distance(p2, p3)
#         d24 = self.distance(p2, p4)
#         d34 = self.distance(p3, p4)
# 
#         arr = [d12, d13, d14, d23, d24, d34]
#         arr.sort()
# 
#         # if it really is a valid square, all of his sides should be truly the same (first 4 elements are the same)
#         #
#         if 0 not in arr and arr[0] == arr[1] == arr[2] == arr[3] and arr[4] == arr[5]:
#             return True
#         return False
# 
#     def distance(self, first_coord, second_coord):
#         #pythagorean theory with  delta y and delta x recpectively
#         return (second_coord[1] - first_coord[1])** 2 + (second_coord[0] - first_coord[0])** 2
# 
#     t= validSquare( p1=[0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1])
#     print(t)


def validSquare(p1, p2, p3, p4) -> bool:
    """

    1/3q and 2/4q musi byt slope 1 and -1 respectively
    1/2q and 3/4q xaxis = 1
    3/2q and 1/4q yaxis = 1
    """

    #6 because four square vertecies can be connected 6ways
    d12 = distance(p1, p2)
    d13 = distance(p1, p3)
    d14 = distance(p1, p4)
    d23 = distance(p2, p3)
    d24 = distance(p2, p4)
    d34 = distance(p3, p4)

    arr = [d12, d13, d14, d23, d24, d34]
    arr.sort()

    # if it really is a valid square, all of his sides should be truly the same (first 4 elements are the same)
    if 0 not in arr and arr[0] == arr[1] == arr[2] == arr[3] and arr[4] == arr[5]:
        return True
    return False

def distance(first_coord, second_coord):
    #pythagorean theory with  delta y and delta x recpectively
    return (second_coord[1] - first_coord[1])** 2 + (second_coord[0] - first_coord[0])** 2

print(validSquare([0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))