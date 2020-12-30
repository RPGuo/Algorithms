import random


def heap_sort(nums):
    if not nums:
        return []
    if len(nums) <= 1:
        return nums

    heap_size = len(nums) - 1
    count = (heap_size - 1) // 2
    for i in range(count + 1):
        heap_adjust(nums, count - i, heap_size)

    for i in range(heap_size):
        nums[0], nums[heap_size - i] = nums[heap_size - i], nums[0]
        heap_adjust(nums, 0, heap_size - i - 1)

    return nums


def heap_adjust(nums, start, end):
    temp = nums[start]
    i = start
    j = 2*i + 1
    while j <= end:
        if j < end and nums[j] < nums[j+1]:
            j = j + 1
        if temp < nums[j]:
            nums[i] = nums[j]
            i = j
            j = 2*i + 1
        else:
            break
    nums[i] = temp


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = heap_sort(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)