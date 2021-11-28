def longestSubString(s):
    l = 0
    hash_s = set()
    max_len = 0
    for r in range(len(s)):
        while s[r] in hash_s:
            hash_s.discard(s[l])
            l+=1
        hash_s.add(s[r])
        max_len = max(max_len, r - l + 1)
    return max_len

print(longestSubString("abcabcbb"))

print(longestSubString("bbbbbb"))

print(longestSubString("pwwkew"))

print(longestSubString("dsgsghshdfgregrrrr"))

print(longestSubString("hgresggfdsf"))

print(longestSubString("shrhtrhsr"))

print(longestSubString(" "))


