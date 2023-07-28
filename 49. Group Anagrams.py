from collections import defaultdict


def groupAnagrams(strs):
    settage = defaultdict(list)

    for s in strs:
        sn = ''.join(sorted(s))
        settage[sn] += [s]

    return settage.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))



'''
    settage = defaultdict(list)

    for s in strs:
        tmp = defaultdict(int)
        sn = ''.join(sorted(s))

        for i in sn:
            tmp[i]+=1

        #settage[str({key: val for key, val in sorted(tmp.items(), key=lambda ele: ele[0])})] += [s]
        settage[str(tmp)] += [s]

    return settage.values()
'''