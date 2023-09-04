"""
Given a string s, find the length of the longest substring
without repeating characters.
(A substring is a contiguous non-empty sequence of characters
within a string.)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        for pos, symbol in enumerate(s):
            all_ch = {symbol}
            current_size = 1
            for next_symbol in s[pos+1:]:
                if next_symbol in all_ch:
                    break
                else:
                    all_ch.add(next_symbol)
                    current_size += 1
            if current_size > max_size:
                max_size = current_size
        return max_size
