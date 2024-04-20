
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

import collections


class Solution:
    '''iterative bfs from booted graph'''
    def getImportance(self, employees, subject: int) -> int:
        importance = collections.defaultdict(int)
        dag=collections.defaultdict(list)

        # for debugging not using the fucking class implementation
        for id, impor, souseds in employees:
            dag[id] = souseds
            importance[id] = impor

        '''
        # for submit matter
        for e in employees:
            dag[e.id] = e.subordinates
            importance[e.id] = e.importance
        '''

        q, noob_o_meter = collections.deque([subject]), 0
        while q:
            nigga = q.popleft()
            noob_o_meter+=importance[nigga]

            for niggbor in dag[nigga]:
                q.append(niggbor)

        return noob_o_meter

def main():
    sol = Solution()
    print(sol.getImportance([[1,2,[]],], 5))
    print(sol.getImportance([[1,2,[]],], 1))
    print(sol.getImportance([[1,5,[2,3]],[2,3,[]],[3,3,[]]], 1))
    print(sol.getImportance([[1,2,[5]],[5,-3,[]]], 5))

if __name__ == "__main__": main()