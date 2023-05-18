class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for x, y in zip(range(0, len(s)), range(len(t)-1, -1, -1)):
            print(x,y)
            print(s[x], t[y])
            if s[x] in chars:
                chars[s[x]] = abs(chars[s[x]] - 1)
            else:
                chars[s[x]] = 1
            if t[y] in chars:
                chars[t[y]] = abs(chars[t[y]] - 1)
            else:
                chars[t[y]] = 1
            print(chars)
        return not any(chars.values())
    

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)