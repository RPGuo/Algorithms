import random


def radix_lsd_sort(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    mod, div = 10, 1
    max_count = len(str(max(nums)))
    buckets = [[] for _ in range(mod)]
    while max_count:
        for i in nums:
            bucket_id = i // div % 10
            buckets[bucket_id].append(i)
        index = 0
        for bucket in buckets:
            while bucket:
                nums[index] = bucket.pop(0)
                index += 1
        div = div * 10
        max_count -= 1
    return nums


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = radix_lsd_sort(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)