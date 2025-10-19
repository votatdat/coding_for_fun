def max_subarray_sum(nums):
    max_ending_here = 0
    max_so_far = 0

    for num in nums:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


# Example Usage
print(max_subarray_sum([34, -50, 42, 14, -5, 86]))  # Output: 137
print(max_subarray_sum([-5, -1, -8, -9]))  # Output: 0
