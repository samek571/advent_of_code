using System;
using System.Collections.Generic;
using System.Linq;

namespace _349._Intersection_of_Two_Arrays
{
    public class Solution {
        public int[] Intersection(int[] nums1, int[] nums2)
        {
            HashSet<int> a = new HashSet<int>(nums1);
            HashSet<int> b = new HashSet<int>(nums2);
            
            return a.Intersect(b).ToArray();
        }
    }
    
    
    internal class Program
    {
        public static void Main(string[] args)
        {
            Solution sol = new Solution();
            Console.WriteLine(string.Join(" ", sol.Intersection(new int[] {1,2,2,1}, new int[] {2,2})));
            Console.WriteLine(string.Join(" ", sol.Intersection(new int[] {4,9,5}, new int[] {9,4,9,8,4})));
            Console.WriteLine(string.Join(" ", sol.Intersection(new int[] {41,91,15}, new int[] {9,4,9,8,4})));
        }
    }
}