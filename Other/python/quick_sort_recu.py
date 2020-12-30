import random


def quick_sort_recu(nums, left, right):
    if not nums or left >= right:
        return []
    l, r, key = left, right, nums[left]
    while l < r:
        while l < r and key <= nums[r]:
            r -= 1
        nums[l] = nums[r]
        while l < r and key >= nums[l]:
            l += 1
        nums[r] = nums[l]
    nums[l] = key
    quick_sort_recu(nums, left, l - 1)
    quick_sort_recu(nums, l + 1, right)
    return nums


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = quick_sort_recu(test_nums, 0, len(test_nums)-1)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)