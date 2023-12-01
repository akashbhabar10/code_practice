def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        print("num_indices",num_indices)
        complement = target - num
        print("complement",complement)
        if complement in num_indices:
            print("True")
            return [num_indices[complement], i]

        num_indices[num] = i
        

    return None

# Example usage:
nums = [ 11,7, 2,15]
target = 9
result = two_sum(nums, target)

if result is not None:
    print("Indices:", result)
else:
    print("No solution found.")
