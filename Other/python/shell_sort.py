import random


def shell_sort(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    gap = 1
    while gap < len(nums) // 2:
        gap = gap * 2 + 1
    while gap > 0:
        for i in range(gap, len(nums)):
            cur_nums, pre_index = nums[i], i-gap
            while pre_index >= 0 and cur_nums < nums[pre_index]:
                nums[pre_index+gap] = nums[pre_index]
                pre_index -= gap
            nums[pre_index+gap] = cur_nums
        gap = gap//2
    return nums


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = shell_sort(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)