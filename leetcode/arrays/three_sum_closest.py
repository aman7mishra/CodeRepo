class Solution:
    def threeSumClosest(self, nums: List[int], ca: int) -> int:
        output = sum(nums[:3])
        nums.sort()

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                sums = sum([nums[i], nums[l], nums[r]])
                dis = abs(ca-sums)
                if abs(ca-output) > dis:
                    output = sums
                if ca>sums:
                    l += 1
                elif ca<sums:
                    r -= 1
                else:
                    return ca
        return output
