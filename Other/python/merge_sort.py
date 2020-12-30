import random


def merge_sort(nums):
    if not nums:
        return []
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merged(left, right)


def merged(left, right):
    l, r, res = 0, 0, []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:] if left[l:] else right[r:]
    return res


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = merge_sort(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)