# Read from the file words.txt and output the word frequency list to stdout.

# import re
# import collections
#
#
#
# origin = open("words.txt")
# pile_of_shit = origin.read().strip().split("\n")
# origin.close()
#
# one_long_line=" ".join(pile_of_shit)
# c=re.split(r"\s+", one_long_line)
#
# hashmap=collections.defaultdict(int)
# for word in c:
# 	x=hashmap.get(word,0)
# 	hashmap[word]=x+1
#
# res=sorted([(key,val) for key, val in hashmap.items()], reverse=True)
#
# for a,b in res:
# 	print(a,b)

python3 <<< 'exec("import re\na=open(\"words.txt\")\nb=a.read().strip()\na.close();z=b.split(\"\\n\");y=\" \".join(z)\nc=re.split(r\"\s+\",y);d=dict()\nfor w in c:x=d.get(w,0);d[w]=x+1\nout=[(w[1],w[0]) for w in list(d.items())];out.sort(reverse=True)\nfor o in out:print(o[1],o[0])")'






#'''THIS ISNT PYTHON '''
# hes=dict()

# for i in file:
#     if i in hes: hes[i]+=1
#     else: hes[i]=1

# res = {key: val for key, val in sorted(hes.items(), key = lambda ele: ele[1], reverse = True)}

# for k, v in res.items():
#     print(k, v)