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
"""
LOGIC:
1.The algorithm keeps two candidates on file to monitor potential majority elements.
2.It discovers two candidates who could be majority elements in the first pass.
3.The second pass checks to see if these candidates appear more than n/3 times.
4.The algorithm takes advantage of the fact that there can only be two majority elements that satisfy the criteria.
5.This algorithm is efficient, with a time complexity of O(n) and a space complexity of O(1), and it is appropriate for the constraints.

ALGORITM:
1.Initialization:To keep track of each candidate's occurrences, initialize two candidate variables (candidate1 and candidate2) and two counters (count1 and count2).
2.Counting the First Pass:
    Go through the array iteratively.
    For each of the following elements:
    If it matches candidate1, count1 will be increased.
    Count2 is increased if it matches candidate2.
    If count1 is 0, the current element is set to candidate1 and count1 is reset to 1.
    If count2 is 0, the current element becomes candidate2 and count2 is reset to 1.
    Decrement both counts if neither count is 0 and the current element does not match either candidate.
3.second pass verification:
    Set the counters (counts 1 and 2) to zero.
    Iterate over the array once more.
    For each of the following elements:
    If it matches candidate1, count1 will be increased.
    Count2 is increased if it matches candidate2.
4.Result:
    Determine whether count1 is greater than n/3. If true, include candidate1 in the output.
    Determine whether count2 is greater than n/3. If true, include candidate2 in the outcome.
5.Sort the Output:
    Sort the results list to ensure that they are in the same order.
"""
















