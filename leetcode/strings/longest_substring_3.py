s = "pwwkew"

i = j = 0
max_len = 0
hash = set()


def longest_substring(s):
    i = j = 0
    max_len = 0
    hash = set()
    for char in s:
        if char in hash:
            while char in hash:
                hash.remove(s[j])
                j += 1
        hash.add(char)
        max_len = max(max_len, i - j + 1)
        i+=1
    return max_len

print(longest_substring(s))
