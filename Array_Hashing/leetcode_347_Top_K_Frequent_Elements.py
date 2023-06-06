"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""


class Solution:
	@staticmethod
	def topKFrequent1(nums: list[int], k: int) -> list[int]:
		all_nums_f = {}
		for num in nums:
			if num not in all_nums_f:
				all_nums_f[num] = 1
			else:
				all_nums_f[num] += 1
				return [kv[0] for kv in sorted(all_nums_f.items(),
				                               key=lambda item: item[1])[-k:]]
        
	@staticmethod
	def topKFrequent2(nums: list[int], k: int) -> list[int]:
		count = {}
		freq = [[] for _ in range(len(nums) + 1)]
		for n in nums:
			count[n] = 1 + count.get(n, 0)
		for n, c in count.items():
			freq[c].append(n)
		res = []
		for i in range(len(freq) - 1, 0, -1):
			for n in freq[i]:
				res.append(n)
				if len(res) == k:
					return res
