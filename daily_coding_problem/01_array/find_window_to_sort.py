def find_window_to_sort(nums):
    n = len(nums)
    left, right = None, None

    # Find first out-of-order from left
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            left = i
            break

    if left is None:
        return (0, 0)  # Already sorted

    # Find first out-of-order from right
    for j in range(n - 1, 0, -1):
        if nums[j] < nums[j - 1]:
            right = j
            break

    # Find min and max in window
    window_min = min(nums[left : right + 1])
    window_max = max(nums[left : right + 1])

    # Expand left boundary
    while left > 0 and nums[left - 1] > window_min:
        left -= 1

    # Expand right boundary
    while right < n - 1 and nums[right + 1] < window_max:
        right += 1

    return (left, right)


# Example Usage
print(find_window_to_sort([3, 7, 5, 6, 9]))  # Output: (1, 3)
print(find_window_to_sort([1, 2, 3, 4, 5]))  # Output: (0, 0)
print(find_window_to_sort([1, 10, 8, 5, 6, 15]))  # Output: (1, 4)
