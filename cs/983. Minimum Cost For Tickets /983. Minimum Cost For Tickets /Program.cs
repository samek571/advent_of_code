using System;
using System.Collections.Generic;

public class Solution {
    public int MincostTickets(int[] days, int[] costs)
    {
        int n = days.Length;
        var dp = new int[days[n-1] + 1];
        var travelDays = new HashSet<int>(days);
        
        for (int i=1; i<=days[n-1]; i++)
        {
            if (!travelDays.Contains(i)) {
                dp[i] = dp[i - 1];
                continue;
            }
            dp[i] = dp[i - 1];
            dp[i] = Math.Min(
                dp[i - 1] + costs[0],
                Math.Min(dp[Math.Max(0, i - 7)] + costs[1],
                dp[Math.Max(0, i-30)] + costs[2]
                ));
        }

        return dp[days[n-1]];
    }
}