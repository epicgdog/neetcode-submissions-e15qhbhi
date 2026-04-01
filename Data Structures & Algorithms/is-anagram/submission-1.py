class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for ch in t:
            if ch in s:
                s = s.replace(ch, "", 1)
                t = t.replace(ch, "", 1)
        return len(s) == 0 and len(t) == 0
        