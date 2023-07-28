class Solution:
    def freqAlphabets(self, s: str) -> str:

        output_string_reversed, i = '', len(s)
        while i > 0:
            i-=1
            if s[i] == "#":
                output_string_reversed += chr(96+int(s[i-2]+s[i-1]))
                i-=2
            else:
                output_string_reversed+= chr(96+int(s[i]))

        return output_string_reversed[::-1]

def main():
    sol = Solution()
    print(sol.freqAlphabets("10#11#12"))
    print(sol.freqAlphabets("1326#"))

if __name__ == "__main__": main()
