"""
Given n non-negative integers representing an elevation map where
the width of each bar is 1,
compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        lb = height[p1]
        rb = height[p2]
        current_h = min(lb, rb)
        r = 0
        while p1 != p2:
            if lb >= rb:
                p2 -= 1
                current_r = height[p2]
                if current_r > rb:
                    rb = current_r
                    current_h = min(lb, rb)
                extra_h = current_h - height[p2]
            else:
                p1 += 1
                current_l = height[p1]
                if current_l > lb:
                    lb = current_l
                    current_h = min(lb, rb)
                extra_h = current_h - height[p1]
            if extra_h > 0:
                r += extra_h
        return r
