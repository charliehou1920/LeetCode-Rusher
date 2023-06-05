'''
给你一个的整数数组 nums, 将该数组重新排序后使 nums[0] <= nums[1] >= nums[2] <= nums[3]... 
'''
def wiggleSort(self, nums: List[int]) -> None:
    nlen = len(nums)
    nums.sort()
    for i in range(nlen - 1):
        if i % 2:
            nums[i], nums[i+1] = nums[i+1], nums[i]

