def count_smaller(nums):
    n = len(nums)
    result = [0] * n
    arr = list(enumerate(nums))  # [(index, value)]

    def merge_sort(pairs):
        if len(pairs) <= 1:
            return pairs
        mid = len(pairs) // 2
        left = merge_sort(pairs[:mid])
        right = merge_sort(pairs[mid:])
        return merge(left, right)

    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                result[left[i][0]] += j
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            result[left[i][0]] += j
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    merge_sort(arr)
    return result


# Example
print(count_smaller([3, 4, 9, 6, 1]))  # [1, 1, 2, 1, 0]
