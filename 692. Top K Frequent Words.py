from collections import defaultdict
class Solution:
    def topKFrequent(words, k: int):

        dicktionary = defaultdict(int)
        for i in words: dicktionary[i] += 1

        sorteddick = sorted(dicktionary.items(), key=lambda x: (-x[1], x[0]))

        return [i[0] for i in sorteddick][:k]


    print(topKFrequent(["i","love","leetcode","i","love","coding"], k = 3))
    print(topKFrequent(["i","love","leetcode","i","love","coding"], k = 2))
    print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))
    print(topKFrequent(["a","a","a","a","a","b"],1))