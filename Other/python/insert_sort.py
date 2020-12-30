import random

# 首先从1位置开始，往前遍历，如果小于前面值则交换；之后2位置、3位置重复前面操作


def insert_sort(nums):
    if not nums:
        return []
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)-1):
        cur_num, pre_index = nums[i+1], i
        while pre_index >= 0 and cur_num < nums[pre_index]:
            nums[pre_index+1] = nums[pre_index]
            pre_index -= 1
        nums[pre_index+1] = cur_num
    return nums


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = insert_sort(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)