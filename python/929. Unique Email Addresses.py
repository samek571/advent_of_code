class Solution:
    def numUniqueEmails(emails) -> int:
        allmails=set()

        for mail in emails:
            splitnuty = mail.split("@")
            prvacastok = splitnuty[0].replace(".", "")

            if "+" in prvacastok:
                prvacastok= prvacastok.split("+")
                prvacastok = prvacastok[0]
            mail = prvacastok + "@" + splitnuty[1]

            if mail not in allmails:
                allmails.add(mail)


        print(allmails)
        return len(allmails)

    print(numUniqueEmails(["test.email+alex@leetcode.com", "test.email@leetcode.com"]))
    print(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
    print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
