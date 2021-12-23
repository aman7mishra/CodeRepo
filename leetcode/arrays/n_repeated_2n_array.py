class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash = set()
        for num in nums:
            if num in hash:
                return num
            else:
                hash.add(num)
