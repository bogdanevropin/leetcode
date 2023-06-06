"""
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            # check if that a start of sequence
            prev = n - 1
            if prev not in numSet:  # start of sequence
                length = 0
                while length + n in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
