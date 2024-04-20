class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        ''' first we do binary search upon first column - we get how many rows are valid
        secondly we do binary search in each of the row we got validated by the first element
        as worst as it gets is logn for the first colum and for each row logm so multiplied
        logn * logm'''

        # which rows are valid
        R,C = len(matrix), len(matrix[0])
        left, right = 0, R-1
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] > target: right = mid-1
            else: left = mid+1
        #matrix[:left] are the valid rows

        # for each valid we do bs
        for row in matrix[:left]:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2

                if row[mid] == target: return True
                elif row[mid] > target: right = mid - 1
                else: left = mid + 1

        return False



def main():
    sol = Solution()
    print(sol.searchMatrix([[1,2],[2,3]], 4))
    print(sol.searchMatrix([[1,2],[2,3]], 2))
    print(sol.searchMatrix([[1,2],[2,3]], 3))
    print(sol.searchMatrix([[1,2],[2,3]], 1))
    print(sol.searchMatrix([[1,2],[2,3]], 0))
    print(sol.searchMatrix([[1,2]], 0))
    print(sol.searchMatrix([[1,2]], 1))
    print(sol.searchMatrix([[1,2]], 2))
    #print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[5,6,9,16,22],[5,13,14,17,24],[18,21,23,26,30]], target = 5))
    #print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))
    #print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))
    #print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))

if __name__ == "__main__": main()
