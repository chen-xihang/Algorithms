"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

LeetCode #169
"""
def bruteForceVoting(nums):
    if not nums:
        return None
    n = len(nums)
    threshold = n//2
    for y in set(nums):
        m = nums.count(y)
        if m > threshold:
            return y
    return None