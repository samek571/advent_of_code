import re

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sliced = sentence.split()
        discount = 1-discount/100

        new=''
        for word in sliced:
            rgxd = re.match("^\$\d+$", word)

            if rgxd:
                new += "$" + str("{:.2f}".format(int(word[1:])*discount)) + " "

            else: new += word + " "


        return new[:-1]


def main():
    sol = Solution()
    print(sol.discountPrices(sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100))
    print(sol.discountPrices(sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 99))
    print(sol.discountPrices(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50))

if __name__ == "__main__": main()