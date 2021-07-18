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
