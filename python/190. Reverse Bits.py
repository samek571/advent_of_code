class Solution:
    def reverseBits(n: int) -> int:

        return int('{0:032b}'.format(n)[::-1], 2)

    print(reverseBits(10100101000001111010011100))
    print(reverseBits(11111111111111111111111111111101))
    print(reverseBits(10011010001111011100111110111101))
