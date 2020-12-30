import random


def counting_sort(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    temp_list = [0] * (max(nums)+1)
    for i in nums:
        # 待排序数组的值和temp_list 索引相同
        temp_list[i] += 1
    index = 0
    for j in range(len(temp_list)):
        while temp_list[j]:
            # 待排序数组的值和temp_list 索引相同
            nums[index] = j
            temp_list[j] -= 1
            index += 1
    return nums


if __name__ == "__main__":
    test_nums = [random.randint(1, 100) for _ in range(10)]
    target = sorted(test_nums)
    test = counting_sort(test_nums)
    print("target: %s" % target)
    print("test: %s" % test)
    res_flag = True if sum([target[i] == test[i] for i in range(len(target))]) == len(target) else False
    print("result: %s" % res_flag)