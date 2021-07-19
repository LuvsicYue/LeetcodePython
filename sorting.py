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


def merge_sort():
    return


def quick_sort():
    return


def heap_sort():
    return


def counting_sort():
    return


def bucket_sort():
    return


def radixSort():
    return
