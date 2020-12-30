import random


def quick_sort_non_recu(nums):
    if not nums:
        return []
    if len(nums) <= 1:
        return nums
    stack = []
    stack.append(len(nums) - 1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(nums, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)
    return nums


def partition(nums, l, r):
    key = nums[l]
    while l < r:
        while l < r and key <= nums[r]:
            r -= 1
        nums[l] = nums[r]
        while l < r and key >= nums[l]:
            l += 1
        nums[r] = nums[l]
    nums[l] = key
    return l


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = quick_sort_non_re(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)