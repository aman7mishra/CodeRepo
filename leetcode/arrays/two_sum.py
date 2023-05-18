"""
Given an array of intergers, find the index of the two elements that add up to the number provided

Input - [1,2,6,9,7], target - 8
"""


def two_sum(arr, target):
    """
    Generates a hashtable to solve the problem.
    """
    result = None
    hash_set = dict()
    for index, number in enumerate(arr):
        difference = target - number
        try:
            result = (hash_set[difference], index)
            break
        except KeyError:
            hash_set[number] = index
    return result

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, number in enumerate(nums):
            if target - number in hash:
                return hash[target-number], index
            else:
                hash[number]= index

print(two_sum([1, 2, 6, 9, 7], 8))
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
