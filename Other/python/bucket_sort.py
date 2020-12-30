import random
from quick_sort_non_recu import quick_sort_non_recu


def bucket_sort(nums, bucket_size=5):
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    max_val, min_val = max(nums), min(nums)
    bucket_count = (max_val-min_val)//bucket_size + 1
    buckets = []
    for i in range(bucket_count):
        buckets.append([])
    for i in nums:
        bucket_id = (i-min_val)//bucket_size
        buckets[bucket_id].append(i)
    nums = []
    for temp in buckets:
        temp = quick_sort_non_recu(temp)
        nums += temp
    return nums


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = bucket_sort(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)