"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


class Solution217:
    @staticmethod
    def containsDuplicate1(nums: list[int]) -> bool:
        return len(nums) > len(set(nums))
    
    @staticmethod
    def containsDuplicate2(nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
