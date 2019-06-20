""" Basic string manipulation
"""
class Solution:
    # def numUniqueEmails(self, emails: List[str]) -> int:
    def numUniqueEmails(self, emails):
        ans = set()
        for email in emails:
            email = email.split("@")
            email[0] = ''.join(email[0].split('.')).split('+')[0]
            ans.add(email[0]+'@'+email[1])
        return len(ans)

s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))