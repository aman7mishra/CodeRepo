class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k: return nums
        dic = {}
        for l in nums:
            if l in dic:
                dic[l] += 1
            else:
                dic[l] = 1
        d = [(dic[key], key) for key in dic]
        d.sort(reverse=True)
        return [p[1] for p in d[:k]]