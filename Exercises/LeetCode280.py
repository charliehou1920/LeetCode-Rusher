'''
给你一个的整数数组 nums, 将该数组重新排序后使 nums[0] <= nums[1] >= nums[2] <= nums[3]... 
'''
def wiggleSort(nums):
    nlen = len(nums)
    nums.sort()
    # 1 2 3 4 5 6
    for i in range(nlen - 1):
        if i % 2:
            nums[i], nums[i+1] = nums[i+1], nums[i]

def main():
    nums =  [3,5,2,1,6,7,4]
    wiggleSort(nums)
    print(nums)

if __name__ == "__main__":
    main()

# Output: [1, 3, 2, 5, 4, 6]