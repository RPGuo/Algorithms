import random

# 遍历 len(nums)-1 次
# 左边为排好序数组，从右边未排序数组选最小值，交换至左边排序数组末尾


def selection_sort(nums):
    if not nums:
        return []
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[index]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    return nums


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = selection_sort(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)