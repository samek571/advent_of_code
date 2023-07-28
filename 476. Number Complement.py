class Solution:
    def findComplement(n: int) -> int:
        return n ^ int('1' * len(bin(n)[2:]), 2)

        new=''
        n_bin = bin(n)[2:]
        for i in str(n_bin):
            if i == "1": new+="0"
            else: new+="1"

        return int(new,2)

    print(findComplement(6))
    print(findComplement(5))
    print(findComplement(1))