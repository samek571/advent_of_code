import collections
from collections import Counter
class Solution:
    def frequencySort(s: str) -> str:
        table=dict()

        #freq=Counter(s).most_common()
        for i in s:
            if i in table: table[i]+=1
            else: table[i]=1

        #print(freq)
        table = {key: val for key, val in sorted(table.items(), key=lambda ele: ele[1], reverse=True)}

        s=''
        for k, v in table.items():
            s += v*k

        return s

    print(frequencySort("tree"))
    print(frequencySort("cccaaaahh"))
    print(frequencySort("Aabb"))
    print(frequencySort("A"))
    print(frequencySort("iuwdfisdunocwieiwfgiujnbqefovjqeorigjhoknjgvoisdkfkwepfojiweogjsdojueiwufnlkxzncoiu"))