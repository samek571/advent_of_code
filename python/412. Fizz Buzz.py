class Solution:
    def fizzBuzz(n: int):
        array = [str(i) for i in range(1, n+1)]

        for i in range (14, n, 15):
            array[i]="FizzBuzz"

        for i in range (2, n, 3):
            if array[i] != "FizzBuzz": array[i] = "Fizz"

        for i in range (4, n, 5):
            if array[i]!="FizzBuzz": array[i]="Buzz"

        return array
    print(fizzBuzz(53))