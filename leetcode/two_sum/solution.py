
def twoSum(nums, target):
    i = 0
    while i < len(nums):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
        i += 1

print(twoSum([3,3], 6))