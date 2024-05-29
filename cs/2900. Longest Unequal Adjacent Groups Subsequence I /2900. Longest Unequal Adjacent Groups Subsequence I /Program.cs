using System.Collections;
using System.Linq;


public class Solution {
    public IList<string> GetLongestSubsequence(string[] words, int[] groups)
    {
        int n = words.Length;
        var dp = new int [n];
        var prev = new int [n];
        for (int tmp = 0; tmp<n; tmp++)
        {
            prev[tmp] = -1;
            dp[tmp] = 1;
        }

        for (int i = 0; i<n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if ((groups[i] != groups[j]) && (dp[i] < dp[j]+1))
                {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
        }

        int l = dp.Max();
        int l_id = Array.IndexOf(dp, l);
        List<string> res = new List<string>();
        while (l_id != -1) {
            res.Add(words[l_id]);
            l_id = prev[l_id];
        }

        res.Reverse();
        return res;
    }
}