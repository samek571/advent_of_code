using System.Collections.Generic;
using System;

namespace _1992._Find_All_Groups_of_Farmland
{
    internal class Program
    {
        public static void Main()
        {
            Solution sol = new Solution();

            int[][] land = new int[][] {
                new int[] { 1, 0, 0, 0, 0, 1, 0, 0 },
                new int[] { 1, 0, 1, 1, 1, 1, 0, 0 },
                new int[] { 0, 0, 1, 1, 1, 1, 0, 0 },
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 1, 1, 1, 1, 0, 0, 1, 1 },
                new int[] { 1, 1, 1, 1, 0, 0, 1, 1 }
            };

            int[][] results = sol.FindFarmland(land);
            foreach (var item in results)
            {
                Console.WriteLine($"[{item[0]}, {item[1]}, {item[2]}, {item[3]}]");
            }
        }
    }


    public class Solution
    {
        public int[][] FindFarmland(int[][] land)
        {
            List<int[]> ans = new List<int[]>();

            int n = land.Length;
            if (n == 0) return ans.ToArray();
            int m = land[0].Length;

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m;)
                {
                    if (land[i][j] == 1)
                    {
                        int jj = j;
                        while (jj < m && land[i][jj] == 1)
                        {
                            jj++;
                        }

                        int ii = i;
                        for (; ii < n && land[ii][j] == 1; ii++)
                        {
                            land[ii][j] = jj + 1;
                        }

                        ans.Add(new int[] { i, j, ii - 1, jj - 1 });
                        j = jj + 1;
                    }
                    else if (land[i][j] == 0)
                    {
                        j++;
                    }
                    else
                    {
                        j = land[i][j];
                    }
                }
            }

            return ans.ToArray();
        }
    }
}