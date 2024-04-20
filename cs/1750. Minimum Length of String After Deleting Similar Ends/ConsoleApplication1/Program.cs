using System;


public class Program
{
    public static void Main(string[] args)
    {
        Solution sol = new Solution();
        Console.WriteLine(sol.MinimumLength("abrrrrrcbbaaa"));
        Console.WriteLine(sol.MinimumLength("abcbbaaa"));
        Console.WriteLine(sol.MinimumLength("abbbaaa"));
        Console.WriteLine(sol.MinimumLength("abbcdddacbaaa"));
    }
}


public class Solution {
    public int MinimumLength(string s)
    {
        int i = 0;
        int j = s.Length - 1;
        while (i < j && s[i] == s[j])
        {
            char curr = s[i]; 
            while (i<=j && s[i] == curr){i++;}
            while (i<=j && s[j] == curr){j--;}
        }
        return j-i+1;
    }
}