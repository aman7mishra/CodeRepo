class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result_arr = []
        for query in queries:
            sum = 0
            nums[query[1]] += query[0]
            for num in nums:
                if num % 2 == 0:
                    sum += num
            result_arr.append(sum)
        return result_arr
