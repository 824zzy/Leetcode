# Hash table+dfs
class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        emap = {}
        imap = {}
        for e in employees:
            imap[e.id] = e.importance
            emap[e.id] = e.subordinates
        self.ans = imap[id]

        def dfs(subs):
            if not subs:
                return
            for sub in subs:
                self.ans += imap[sub]
                dfs(emap[sub])

        dfs(emap[id])
        return self.ans
