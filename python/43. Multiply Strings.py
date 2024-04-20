class Solution:
    def multiply(num1: str, num2: str) -> str:
        dick = {"1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
                }

        n=0
        for digit in num1:
           n = 10*n+dick[digit]

        m=0
        for digit in num2:
           m = 10*m+dick[digit]

        return str(m*n)

    print(multiply("123", "456"))
