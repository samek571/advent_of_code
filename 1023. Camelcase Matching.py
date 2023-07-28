import re

class Solution:
    def camelMatch(self, queries, pattern: str):
        # upd = ''
        # for c in pattern:
        #     upd+=c+"[a-z]{0,}"
        # print(upd)
        #
        # o=[]
        # for s in queries:
        #     x= re.match(upd, s)
        #     print(x)
        #
        #     if x: o.append(True)
        #     else: o.append(False)
        #
        # print("\n")
        # return o

        #r and _r_r_r_r
        return [re.fullmatch('[a-z]*' + '[a-z]*'.join(pattern) + '[a-z]*', q) for q in queries]


def main():
    sol = Solution()
    print(sol.camelMatch(queries = ["FooBarTest","FooB"], pattern = "FB"))
    print("\n\n\n\n")
    print(sol.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"))
    print(sol.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"))
    print(sol.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"))

if __name__ == "__main__": main()