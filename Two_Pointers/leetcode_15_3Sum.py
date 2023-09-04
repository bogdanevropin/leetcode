"""
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i1, a in enumerate(nums):
            if i1 > 0 and a == nums[i1 - 1]:
                continue
            i2, i3 = i1 + 1, len(nums) - 1
            while i2 < i3:
                s = a + nums[i2] + nums[i3]
                if s < 0:
                    i2 += 1
                elif s > 0:
                    i3 -= 1
                else:
                    res.append([a, nums[i2], nums[i3]])
                    i2 += 1
                    while nums[i2] == nums[i2 - 1] and i2 < i3:
                        i2 += 1
        return res
    