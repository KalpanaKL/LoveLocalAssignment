import ast

def major_ele(nums):
    if not nums:
        return []

    # Initialize candidates and counters
    candidate1, candidate2, count1, count2 = None, None, 0, 0

    # Count occurrences of candidates
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Reset counters for a second pass
    count1, count2 = 0, 0

    # Count occurrences of candidates in the second pass
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    # Check if candidates appear more than n/3 times
    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    # Sort the result for consistent order
    result.sort()

    return result

# Take input from the user in the format [num1, num2, num3, ...]
user_input = input("nums= ")

# Safely parse the input string as a list of integers
nums = ast.literal_eval(user_input)

# Example usage with the user's input
result = major_ele(nums)
print(result)

