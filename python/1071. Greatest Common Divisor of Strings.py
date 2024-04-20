class Solution:
    '''To find the largest string x that divides both str1 and str2, we can use the GCD (Greatest Common Divisor) approach. The idea is to find the longest common prefix between str1 and str2 and then keep removing this prefix from both strings until either one of them becomes empty. The remaining string is then concatenated with the common prefix to get the result.'''
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        if str1 == str2: return str1
        
        if str1[:len(str2)] != str2: return ""
        
        return self.gcdOfStrings(str1[len(str2):], str2)
