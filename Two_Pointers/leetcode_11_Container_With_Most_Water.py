"""
ou are given an integer array height of length n.
There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        lb = height[p1]
        rb = height[p2]
        max_a = min(lb, rb) * p2
        while p1 + 1 != p2:
            if lb < rb:
                p1 += 1
                lb = height[p1]
            else:
                p2 -= 1
                rb = height[p2]
            new_a = min(lb, rb) * (p2 - p1)
            if max_a < new_a:
                max_a = new_a
        return max_a
