"""
Given an integer array nums,
return an array answer such that answer[i] is equal to the product of
all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        all_product = 1
        zeros_count = 0
        for n in nums:
            if n == 0:
                zeros_count += 1
            else:
                all_product *= n
        if zeros_count >= 2:
            return [0]*len(nums)
        elif zeros_count == 1:
            return [all_product if n == 0 else 0 for n in nums]
        else:
            return [all_product // n for n in nums]
