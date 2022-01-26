
def longestPalindrome(s):
    ans = ""
    for i in range(len(s)):
        odd = check(s,i,i)
        even = check(s,i,i+1)
        ans = max(ans, odd, even, key=len)
    return ans

def check(s,l,r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]