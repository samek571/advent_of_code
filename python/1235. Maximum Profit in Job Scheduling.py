class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
            . return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

            . we need loohahead , greedy wont work since greedy will try occupying blank spaces while maybe it might make sence to not

            . dp(ci):
                take ci or donot

        """

        sep = sorted([(st, en, pr) for st, en, pr in zip(startTime, endTime, profit)])

        @lru_cache(None)
        def dp(ci):
            if ci >= len(sep):
                return 0  # reached end

            return max(
                dp(ci + 1),
                sep[ci][2] + dp(bisect_left(sep, (sep[ci][1],)))
            )

        return dp(0)