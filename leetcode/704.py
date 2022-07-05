def search(nums: list[int], target: int) -> int:
    end = len(nums) - 1
    start = 0
    middle = (start + end) // 2

    while True:
        if target > nums[middle]:
            start = middle + 1
            middle = (start + end) // 2
        elif target < nums[middle]:
            end = middle
            middle = (start + end) // 2
        elif target == nums[middle]:
            return middle
        if start >= end:
            break
    if target == nums[middle]:
            return middle
    return -1


print(search([-1,0,5], -1))