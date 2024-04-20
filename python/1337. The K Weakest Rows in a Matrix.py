class Solution:
    def kWeakestRows(self, mat, k: int):

        alll={}
        for i, row in enumerate(mat):

            flag = True
            if row[-1] == 1:
                alll[i] = len(row)
                flag = False

            elif row[0] == 0:
                alll[i] = 0
                flag = False

            left, right = 0, len(row) - 1
            while flag and left <= right:
                mid = (left + right) // 2

                if row[mid] == 1 and row[mid+1] == 0:
                    alll[i] = (mid+1)
                    break

                elif row[mid] == 1 and row[mid+1] == 1:
                    left = mid + 1

                else:
                    right = mid - 1

        strength_dict = dict(sorted(alll.items(), key=lambda item: item[1]))
        return list(strength_dict.keys())[:k]



def main():
    sol = Solution()
    print(sol.kWeakestRows( mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))
    print(sol.kWeakestRows(mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))

if __name__ == "__main__": main()