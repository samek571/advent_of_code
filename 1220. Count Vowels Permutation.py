class Solution:
    def countVowelPermutation(self, n: int) -> int:
        #its more of a visual problem but we draw up where can we get from each letter and it turns out that some paths are repeating (obviously), if we track from which all letters are we able to get to one letter in particular, we get the answer.
        #example: to i we can get only from o and e, therefore we are able to move by one step, and we are able to do n steps.

        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            #it has to happen simultaneosly because AS IF we are doing endless painful bfs in which we are moving by levels
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

        return (a + e + i + o + u) % (10**9 + 7)
