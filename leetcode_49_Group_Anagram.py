"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by
rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


class Solution49:
	@staticmethod
	def anagrams(inp1: str, inp2: str) -> bool:
		# if the length of the two strings is not the same,
		# they are not anagrams.
		if len(inp1) != len(inp2):
			return False
		# initialize the dictionary
		counts = {}
		# loop simultaneously through the characters of the two strings.
		for c1, c2 in zip(inp1, inp2):
			if c1 in counts.keys():
				counts[c1] += 1
			else:
				counts[c1] = 1
			if c2 in counts.keys():
				counts[c2] -= 1
			else:
				counts[c2] = -1
		for count in counts.values():
			if count != 0:
				return False
		return True
	
	@staticmethod
	def groupAnagrams1(strs: list[str]) -> list[list[str]]:
		str_dict = {}
		for word in strs:
			s_word = str(sorted(word))
			if s_word not in str_dict:
				str_dict[s_word] = [word]
			else:
				str_dict[s_word].append(word)
		all_s_strs = []
		for s_k in str_dict:
			all_s_strs.append(str_dict[s_k])
		return all_s_strs
	
	