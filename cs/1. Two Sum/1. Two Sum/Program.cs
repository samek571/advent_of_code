using System;
using System.Collections;

namespace _1._Two_Sum
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Solution sol = new Solution();
            Console.WriteLine(string.Join(" ", sol.TwoSum(new int[] { 2, 7, 11, 15 }, 9)));
            Console.WriteLine(string.Join(" ", sol.TwoSum(new int[] { 3, 2, 4 }, 7)));
            Console.WriteLine(string.Join(" ", sol.TwoSum(new int[] { 3, 2, 4 }, 6)));
            Console.WriteLine(string.Join(" ", sol.TwoSum(new int[] { 4, 4, 2, 6 }, 8)));
            
            //these wont happen, otherwise would have been solved by null exception
            //Console.WriteLine(string.Join(" ", sol.TwoSum(new int[] { 3, 4 }, 6)));
            //Console.WriteLine(string.Join(" ", sol.TwoSum(new int[] { 3, 4, 9, 2 }, 66)));
        }
    }

    public class Solution
    {
        public int[] TwoSum(int[] nums, int target)
        {
            Hashtable dick = new Hashtable();
            for (int i = 0; i < nums.Length; i++)
            {
                if (dick.ContainsKey(target - nums[i]))
                {
                    return new int[] { i, (int)dick[target-nums[i]]};
                }

                dick[nums[i]] = i;
            }
            return null;
        }
    }
}