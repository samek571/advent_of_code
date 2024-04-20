class Solution:
    def intToRoman(num: int) -> str:
        output=''

        while num >=0:
            if num-1000 >= 0:
                num-=1000
                output+="M"
                continue
            elif num-900 >= 0:
                num-=900
                output+="CM"
                continue
            elif num-500 >= 0:
                num-=500
                output+="D"
                continue
            elif num-400 >= 0:
                num-=400
                output+="CD"
                continue
            elif num-100 >= 0:
                num-=100
                output+="C"
                continue
            elif num-90 >= 0:
                num-=90
                output+="XC"
                continue
            elif num-50 >= 0:
                num-=50
                output+="L"
                continue
            elif num-40 >= 0:
                num-=40
                output+="XL"
                continue
            elif num- 10 >= 0:
                num -= 10
                output += "X"
                continue
            elif num- 9 >= 0:
                num -= 9
                output += "IX"
                continue
            elif num- 5 >= 0:
                num -= 5
                output += "V"
                continue
            elif num- 4 >= 0:
                num -= 4
                output += "IV"
                continue
            elif num- 1 >= 0:
                num -= 1
                output += "I"
                continue
            if num == 0:
                return output

    print(intToRoman(1994))