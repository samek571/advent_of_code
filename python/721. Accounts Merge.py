import collections
class Solution:
    def accountsMerge(self, accounts):# -> List[List[str]]:
        import collections
        class Solution:
            def accountsMerge(self, accounts):  # -> List[List[str]]:
                # data = collections.defaultdict(list)

                # for case in accounts:
                #     name = case[0]

                #     # completly new case
                #     if name not in data:
                #         data[name] += [(set(case[1:]))]

                #     # multiple fucking johns
                #     else:
                #         dudes_emails = set(case[1:]);
                #         new = True
                #         for known in data[name]:
                #             if len(known & dudes_emails)>0:
                #                 known |= dudes_emails
                #                 new = not new
                #                 break

                #         # not known person --> new
                #         if new:
                #             data[name] += [(set(case[1:]))]

                # # output form stylistics
                # o = []
                # for name, shits in data.items():
                #     for emails in shits:
                #         #o.append([name] + sorted([i for i in emails]))
                #         o.append([name] + [i for i in sorted(emails)])

                # return o

                # AccountDict stores doubly directed email linked to head of the email list
                accountDict = defaultdict(set)
                emailToNameDict = {}
                result = []

                # Build both the dictionaries
                for account in accounts:
                    accName = account[0]
                    emailHead = account[1]

                    for i in range(1, len(account)):
                        currEmail = account[i]

                        accountDict[emailHead].add(currEmail)
                        accountDict[currEmail].add(emailHead)
                        emailToNameDict[currEmail] = accName

                # Traverse dfs of the graph to find emails that are connected to this email
                def dfs(currEmail, mergedAcc):
                    if currEmail in visited:
                        return

                    visited.add(currEmail)
                    mergedAcc.append(currEmail)
                    for neighbor in accountDict[currEmail]:
                        dfs(neighbor, mergedAcc)

                    return mergedAcc

                # visited set to ensure we do not visit and already visited node
                visited = set()
                for email in emailToNameDict:
                    if email not in visited:
                        result.append([emailToNameDict[email]] + sorted(dfs(email, [])))

                return result

def main():
    sol = Solution()
    print(sol.accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
    print(sol.accountsMerge(accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))
    print(sol.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))

if __name__ == "__main__": main()