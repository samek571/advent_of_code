using System;
using System.Collections.Generic;
using System.Linq;

namespace _1291._Sequential_Digits
{
    public class Solution {
        public IList<int> SequentialDigits(int low, int high)
        {
            List<int> res = new List<int>();
            for (int i = 1; i < 10; i++)
            {
                int summage = 0;
                for (int j = i; j < 10; j++)
                {
                    summage = summage * 10 + j;
                    if (summage >= low && summage <= high)
                    {
                        res.Add(summage);
                    }
                }
            }

            return res.OrderBy(x => x).ToList();
        }
    }
    
    
    internal class Program
    {
        public static void Main(string[] args)
        {
            Solution sol = new Solution();
            Console.WriteLine(string.Join(" ",sol.SequentialDigits(100 , 300)));
            Console.WriteLine(string.Join(" ",sol.SequentialDigits(1000 , 13000)));
        }
    }
}