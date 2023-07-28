class Solution:
    def romanToInt(s: str) -> int:
        roman=["I", "V", "X", "L", "C", "D", "M"]
        decimal=[1, 5, 10, 50, 100, 500, 1000]
        output = 0

        if "IV" in s or "IX" in s or "XL" in s or "XC" in s or "CD" in s or "CM" in s:
            s += "NNN"
            i=0
            while i<len(s):
                # iterujeme s a vzdy pre s[i] sa pozrieme, na s[i+1] ci niesu IV IX XL... ak ano, s[0] pripocitame k outputu a s[i+1] taktiez,
                # potom i+=2 a valime az dokym nenatrafime na "NN" na konci, ak nie; tak pripocitame s[i] a spravime i+=1
                #if digit_index
                temporarhovno = ""
                temporarhovno += s[i]
                temporarhovno += s[i+1]
                if temporarhovno=="IV":
                    output+=4
                    i += 2
                    continue
                elif temporarhovno=="IX":
                    output+=9
                    i += 2
                    continue
                elif temporarhovno=="XC":
                    output+=90
                    i += 2
                    continue
                elif temporarhovno=="XL":
                    output+=40
                    i += 2
                    continue
                elif temporarhovno=="CM":
                    output+=900
                    i += 2
                    continue
                elif temporarhovno == "CD":
                    output += 400
                    i += 2
                    continue

                if "NN" in temporarhovno:
                    return output

                if "N" in temporarhovno:
                    c=decimal[roman.index(temporarhovno[0])]
                    output+=c
                    return output

                if "N" not in temporarhovno:
                    c=decimal[roman.index(temporarhovno[0])]
                    output+=c

                i+=1

        else:
            for i in range(len(s)):
                digit_index = roman.index(s[i])
                output+=decimal[digit_index]

            return output
    print(romanToInt("CMXLIII"))
    print(romanToInt("DCCCXLV"))