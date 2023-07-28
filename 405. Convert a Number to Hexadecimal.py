class Solution:
    def toHex(num: int) -> str:
        return hex(num)[2:] if num>0 else hex(num % 2**32)[2:]

    print(toHex(26))
    print(toHex(2633))
    print(toHex(-1))
    print(toHex(-14))
    print(toHex(-17))
    print(toHex(0))