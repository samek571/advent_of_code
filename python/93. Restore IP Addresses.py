class Solution:
    '''obvious backtracking recursion'''
    # there are 4 segments of at most 3 numbers
    # no leading 0 unless its 0 only
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)>12: return []
        
        def dfs(idx, path:list): 
            #exit
            if idx>= len(s):
                if len(path) == 4:
                    seen.add(".".join(path))
                
                return

            #depth
            for segment in range(1, 4):
                curent_shit = s[idx:idx+segment]

                if curent_shit[0]=="0" and len(curent_shit)>=2: continue
                
                if 0<= int(curent_shit) <=255 and len(path)<4:
                    dfs(idx+segment, path + [curent_shit])


        seen = set()
        dfs(0, [])
        return seen


