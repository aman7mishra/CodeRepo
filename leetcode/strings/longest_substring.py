def longestSubString(s):
    max_len = 0
    current_len = 0
    h_map = {}
    for index in range(len(s)):
        char = s[index]
        if char in h_map:
            current_len = max(current_len, h_map[char]+1)
        h_map[char] = index
        max_len = max(max_len, index-current_len+1)
    return max_len

print(longestSubString("abcabcbb"))

print(longestSubString("bbbbbb"))

print(longestSubString("pwwkew"))

print(longestSubString("dsgsghshdfgregrrrr"))

print(longestSubString("hgresggfdsf"))

print(longestSubString("shrhtrhsr"))

print(longestSubString(" "))


