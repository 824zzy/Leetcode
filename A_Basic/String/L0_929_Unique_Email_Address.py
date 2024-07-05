""" https://leetcode.com/problems/unique-email-addresses/
Basic string usage
"""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0].replace(".", "")
            seen.add("@".join([local, domain]))
        return len(seen)


s = Solution()
print(
    s.numUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
    )
)
