class Solution:
    def reverseWords(s: str) -> str:
        s=s.split()
        print(s)
        print(len(s))

        output=""
        i=len(s)-1
        while i!=0:
            output+=s[i]
            output+= " "
            i-=1
        output+=s[0]

        return output

    print(reverseWords("the sky is   blue"))
    print(reverseWords("the sky is blue"))
    print(reverseWords("  hello world  "))
    print(reverseWords("Alice does not even like bob"))
    print(reverseWords("  Bob    Loves    Alice   "))
    print(reverseWords("    kolac   "))