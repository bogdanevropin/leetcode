"""
Given two strings s and t,
return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase
formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


class Solution242:
	@staticmethod
	def isAnagram1(s: str, t: str) -> bool:
		return sorted(s) == sorted(t)
	
	@staticmethod
	def isAnagram2(s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		count_s, count_t = {}, {}
		for i in range(len(s)):
			count_s[s[i]] = 1 + count_s.get(s[i], 0)  # if key doesn't exist default 0
			count_t[t[i]] = 1 + count_t.get(t[i], 0)
		for c in count_s:
			if count_s[c] != count_t[c].get(c, 0):
				return False
		return True
		