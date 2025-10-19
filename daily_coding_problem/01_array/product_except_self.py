def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for j in range(n - 1, -1, -1):
        result[j] *= suffix
        suffix *= nums[j]
    return result


# Example Usage
print(product_except_self([1, 2, 3, 4, 5]))
print(product_except_self([4, 7, 3]))
