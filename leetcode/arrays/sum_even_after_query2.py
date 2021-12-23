class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        array_of_sums = []
        current_sum = 0
        for num in nums:
            if num % 2 == 0: current_sum += num
        
        for val, ind in queries:
            if nums[ind] % 2 == 0 and val % 2 == 0:
                current_sum += val
            elif nums[ind] % 2 != 0 and val % 2 != 0:
                current_sum += nums[ind] + val
            elif nums[ind] % 2 == 0 and val % 2 != 0:
                current_sum -= nums[ind]
            nums[ind] += val
            array_of_sums.append(current_sum)
        return array_of_sums
