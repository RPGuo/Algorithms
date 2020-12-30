import random

# 遍历 len(nums)-1 次
# 每次从0开始遍历，相邻元素大者往后移动，最终冒泡到数组最右侧


def bubble_sort(nums):
    if not nums:
        return []
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        is_sort = True
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_sort = False
        if is_sort:
            break
    return nums


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = bubble_sort(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)
