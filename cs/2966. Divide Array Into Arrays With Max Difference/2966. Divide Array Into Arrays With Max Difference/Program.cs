using System;
using System.Linq;
using System.Index;
using System.Range;
using System.Collections.Generic;

namespace _2966._Divide_Array_Into_Arrays_With_Max_Difference
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Solution sol = new Solution();
            Print2DArray(sol.DivideArray(new int[] {1,3,4,8,7,9,3,5,1}, 2));
            Print2DArray(sol.DivideArray(new int[] {1,3,3,2,7,3}, 3));
        }

        private static void Print2DArray(int[][] array) {
            foreach (int[] subArray in array) {
                Console.WriteLine("[" + string.Join(", ", subArray) + "]");
            }
            if (array.Length == 0) {
                Console.WriteLine("[]");
            }
            Console.WriteLine(); // Adds an empty line for better readability between cases
        }
    }
    
    public class Solution {
        public int[][] DivideArray(int[] nums, int k)
        {
            Array.Sort(nums);
            List<int[]> res = new List<int[]>();

            for (int i = 2; i < nums.Length; i+=3)
            {
                int[] curr = {nums[i - 2], nums[i - 1], nums[i]};
                //int[] curr = nums[(i-2)..(i+1)];
                Console.WriteLine(string.Join(" ", curr));

                if (nums[i] - nums[i-2] <= k)
                {
                    res.Add(curr);
                }
                else
                {
                    return new int[][] {};
                }
            }

            return res.ToArray();
        }
    }
    
}