class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        interm_ans = [nums[i] for i in range(len(nums))]
        return interm_ans + interm_ans
