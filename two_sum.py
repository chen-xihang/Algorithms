def two_sum(nums, target):
    hashmap = {}
    for i, nums in enumerate(nums):
        complement = target - nums
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums] = i
    return []

nums = [2, 11, 15, 7]
target = 9
two_sum(nums, target)