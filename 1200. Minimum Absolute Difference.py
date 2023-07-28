class Solution:
    def minimumAbsDifference(self, arr):
        min_element, max_element  = arr[0], arr[-1]
        for i in arr:
            min_element = min(min_element, i)
            max_element = max(max_element, i)

        shift = -min_element
        line = [0] * (max_element - min_element + 1)
        answer = []

        for num in arr:
            line[num + shift] = 1

        min_pair_diff = max_element - min_element
        prev = 0

        for curr in range(1, max_element + shift + 1):
            if line[curr] == 0: continue

            if curr - prev == min_pair_diff:
                answer.append([prev - shift, curr - shift])

            elif curr - prev < min_pair_diff:
                answer = [[prev - shift, curr - shift]]
                min_pair_diff = curr - prev

            prev = curr

        return answer


def main():
    sol = Solution()
    print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))

if __name__ == "__main__": main()