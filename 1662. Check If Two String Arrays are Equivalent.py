
def arrayStringsAreEqual(word1, word2) -> bool:
    
    s1, s2 = "", ""
    for i in word1:
        s1 = s1+i
    
    for j in word2:
        s2 = s2+j

    return s1 == s2
    
print(arrayStringsAreEqual(["asd", "asss", "gjie"], ["pqq", "dsf"]))