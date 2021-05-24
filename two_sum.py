#input = [1, 4, 8, 3] target = 5
#output = [0, 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = dict()
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in bucket:
                result = [bucket[diff], index]
            else:
                bucket[nums[index]]=index
        return result
