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
sorted_array = [0.1, 0.5, 1.2, 2.3, 3.5, 4.7, 5.9, 10, 11, 12, 13]
target_value = 7.0

sorted_array = [3, 4.7, 9.9, 12.7, 14, 18.5, 33.5, 34.1, 38.5, 39.9, 44.7]
target_value = 3.0

result = test_binary_search_upper(sorted_array, target_value)

print(type(result))

if result[1] is not None:
    print(f"Number of iterations required: {result[0]}")
    print(f"Upper limit for the target value {target_value}: {result[1]}")
else:
    print(f"Target value {target_value} not found. Upper limit: {sorted_array[-1]}")


test_case = [3, 4.7, 9.9, 12.7, 14, 18.5, 33.5, 34.1, 38.5, 39.9, 44.7]

def test_binary_search_upper():
    assert test_binary_search_upper(test_case, 0)[1] != 3, "Wrong upper limit for first element 3"
    assert test_binary_search_upper(test_case, 50)[1] is None, "No handling for search of elements bigger than max 44.7 in list"
    assert test_binary_search_upper(test_case, 10)[1] != 12.7, "Wrong upper limit for element 10"
    assert test_binary_search_upper(test_case, 34.1)[1] != 34.1, "Wrong upper limit for element 34.1"
    assert test_binary_search_upper(test_case, 18.5)[0] != 1, "First element in the middle that is equal to searched value should be found in first iteration"    


test_binary_search_upper()    
