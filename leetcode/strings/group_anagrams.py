class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        for str in strs:
            res = "".join(sorted(str))
            if res in sets:
                sets[res].append(str)
            else:
                sets[res] = [str]
        return sets.values()