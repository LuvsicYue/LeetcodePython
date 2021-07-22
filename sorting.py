import math
from typing import List


def swap(nums: List[int], i: int, j: int) -> None:
    nums[i], nums[j] = nums[j], nums[i]


def bubble_sort1(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
    return nums


def bubble_sort2(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in reversed(range(n)):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
    return nums


def bubble_sort3(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(1, n):
        for j in range(n - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def selection_sort1(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        max_index = 0
        for j in range(n - i):
            if nums[j] > nums[max_index]:
                max_index = j
        # Put the max num at the end of the array
        nums[max_index], nums[n - i - 1] = nums[n - i - 1], nums[max_index]
    return nums


def selection_sort2(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums


def insertion_sort1(nums):
    n = len(nums)
    for i in range(n): # Effective starting from n = 1
        pre_index = i - 1
        current = nums[i]
        while pre_index >= 0 and nums[pre_index] > current:
            nums[pre_index + 1] = nums[pre_index]
            pre_index -= 1
    return nums


def insertion_sort2(nums):
    n = len(nums)
    for i in range(n): # Effective starting from n = 1
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


def shell_sort1(nums: List[int]) -> List[int]:
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)): # insertion sort part
            current = nums[i]
            pre_index = i - gap
            while pre_index >= 0 and nums[pre_index] > current:
                nums[pre_index + gap] = nums[pre_index]
                pre_index -= gap
        gap //= 2
    return nums


def shell_sort2(nums):
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for i in range(gap):
            for j in range(gap + i, n, gap):
                while j > i and nums[j] < nums[j - gap]:
                    nums[j], nums[j - gap] = nums[j - gap], nums[j]
                    j -= gap
        gap //= 2
    return nums


def __merge_helper(left: List[int], right: List[int]) -> List[int]:
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result


def merge_sort(nums):
    n = len(nums)
    if n < 2:
        return nums
    middle = n // 2
    left, right = nums[0:middle], nums[middle:]
    return __merge_helper(left, right)


def __partition(nums, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if nums[i] < nums[pivot]:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
        i += 1
    nums[pivot], nums[index - 1] = nums[nums - 1], nums[pivot]
    return index - 1


def quick_sort1(nums, left=None, right=None):
    if len(nums) < 2:
        return nums
    left = 0 if left is None else left
    right = len(nums) - 1 if right is None else right
    if left < right:
        partition_index = __partition(nums, left, right)
        quick_sort1(nums, left, partition_index - 1)
        quick_sort1(nums, partition_index + 1, right)
    return nums

def quick_sort(nums):
    return quick_sort2(nums, 0, len(nums) - 1)


def quick_sort2(nums, left=None, right=None):
    if left >= right:
        return nums
    pivot = left
    lo, hi = left + 1, right
    while lo <= hi:
        if nums[lo] > nums[pivot]:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            hi -= 1
        else:
            lo += 1
    lo -= 1
    nums[pivot], nums[lo] = nums[lo], nums[pivot]
    quick_sort2(nums, left, lo - 1)
    quick_sort2(nums, lo + 1, right)
    return nums


def __heapify(nums, i):
    pass


def heap_sort():
    return


def counting_sort():
    return


def bucket_sort():
    return


def radixSort():
    return
