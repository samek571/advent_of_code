class Solution:
    def newInteger(self, n):

        answer = 0 ; lenght = 1 #doing 1-9, 10-99, 100-999 ...
        while n:
            #every 9th number is a bad number therefore base 9 system is relevant since 0-8 the only chars that exist
            n, m = n//9, n%9
            answer += (m * lenght) # converting back to base 10 system

            #doing 1-9, 10-99, 100-999 ...
            lenght*=10

        return answer


def main():
    sol = Solution()
    print(sol.newInteger(965))
    print(sol.newInteger(100))

if __name__ == "__main__": main()