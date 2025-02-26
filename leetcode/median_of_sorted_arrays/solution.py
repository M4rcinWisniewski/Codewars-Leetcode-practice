#Leetcode hard
#https://leetcode.com/problems/median-of-two-sorted-arrays

def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    nums = nums1 + nums2
    nums.sort()
    length_of_two_arrays = m + n
    if length_of_two_arrays % 2 == 0:
        return (nums[length_of_two_arrays // 2 - 1] + nums[length_of_two_arrays // 2]) / 2
    return nums[length_of_two_arrays // 2]



print(findMedianSortedArrays([2, 3],[]))

