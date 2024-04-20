using System;
using System.Collections.Generic;
using System.Linq;

namespace _2540._Minimum_Common_Value
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Solution sol = new Solution();
            
            Console.WriteLine(sol.GetCommon(new int[]{1,2,3}, new int[]{2,4}));
            Console.WriteLine(sol.GetCommon(new int[]{1,2,3,6}, new int[]{2,3,4,5}));
            Console.WriteLine(sol.GetCommon(new int[]{1,5,6}, new int[]{2,3,4}));
        }
    }
    
    public class Solution {
        public int GetCommon(int[] nums1, int[] nums2)
        {
            HashSet<int> a = new HashSet<int>(nums1);
            HashSet<int> b = new HashSet<int>(nums2);
            
            int[] common = a.Intersect(b).ToArray();
            if (common.Length > 0)
            {
                return common.Min();
            }

            return -1;
        }
    }
    
}