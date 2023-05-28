"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
	@staticmethod
	def twoSum1(nums: list[int], target: int) -> list[int]:
		for p1, n1 in enumerate(nums):
			for p2, n2 in enumerate(nums[p1+1:]):  # slice with index not checked
				s = n1 + n2
				if s == target:
					return [p1, p1 + p2 + 1]
	
	@staticmethod
	def twoSum2(nums: list[int], target: int) -> list[int]:
		prev_map = {}  # val: index
		for i, n in enumerate(nums):
			diff = target - n
			if diff in prev_map:
				return [prev_map[diff], i]
			prev_map[n] = i
