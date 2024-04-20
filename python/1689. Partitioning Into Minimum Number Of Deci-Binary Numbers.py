class Solution:
    def minPartitions(n: str) -> int:
        # output=0
        # for i in n: output=max(output, int(i))
        # return output

        return max(n)
    print(minPartitions("32"))
    print(minPartitions("82734"))
    print(minPartitions("27346209830709182346"))
    print(minPartitions("111111111111111111111112"))