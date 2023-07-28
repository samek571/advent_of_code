class Solution:
    def searchMatrix(self, matrix, target):
        hl = len(matrix[0])
        vl = len(matrix)
        i=[]

        left, right = 0, vl-1
        while left <= right:
            mid = (left + right) // 2

            if target>=matrix[mid][0] and target<=matrix[mid][hl-1]:
                i=matrix[mid]
                break

            elif matrix[mid][0] > target: right = mid-1
            else: left = mid+1


        #particular matrix[0]
        left, right = 0, len(i) - 1
        while left <= right:
            mid = (left + right) // 2

            if i[mid] == target: return True
            elif i[mid] > target: right = mid - 1
            else: left = mid + 1

        return False



def main():
    sol = Solution()
    print(sol.searchMatrix([[1,3,5],[10,11,16],[23,30,34],[45,55,56],[57,59,60]], target = 30))
    print(sol.searchMatrix([[1],[5]], 5))
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))

if __name__ == "__main__":
    main()