def max_subarray_sum_circular(nums):
    def kadane(arr):
        max_ending = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending = max(x, max_ending + x)
            max_so_far = max(max_so_far, max_ending)
        return max_so_far

    max_normal = kadane(nums)
    if max_normal < 0:
        return max_normal

    total_sum = sum(nums)
    min_subarray = kadane([-x for x in nums])
    max_circular = total_sum + min_subarray  # total_sum - (-min_sum)
    return max(max_normal, max_circular)


# Example Usage
print(max_subarray_sum_circular([8, -1, 3, 4]))  # 15
