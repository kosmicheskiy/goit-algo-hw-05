def test_binary_search_upper(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_limit = None

    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1

        if arr[mid] == target:
            upper_limit = arr[mid]
            return iterations, upper_limit
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_limit = arr[mid]
            right = mid - 1

    return (iterations, upper_limit)

# Example usage:
sorted_array = [3, 4.7, 9.9, 12.7, 14, 18.5, 33.5, 34.1, 38.5, 39.9, 44.7]
target_value = 4.0

result = test_binary_search_upper(sorted_array, target_value)

print(type(result))

if result[1] is not None:
    print(f"Number of iterations required: {result[0]}")
    print(f"Upper limit for the target value {target_value}: {result[1]}")
else:
    print(f"Target value {target_value} not found. Upper limit: {sorted_array[-1]}")
