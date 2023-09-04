"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where
1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1 = 0
        p2 = len(numbers) - 1
        find = True
        while find:
            sum = numbers[p1] + numbers[p2]
            if sum < target:
                p1 += 1
            elif sum == target:
                return [p1 + 1, p2 + 1]
            elif sum > target:
                p2 -= 1
