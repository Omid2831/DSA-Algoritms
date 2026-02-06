from typing import List

# Array of integers to search through
nums = [2, 7, 11, 15]
# Target sum: find two numbers in nums that add up to this value
target = 9

def two_sum(nums: List[int], target: int) -> List[int]:
    # Create a dictinary to store the indices of the numbers
    numbers = {}

    # Loop through the List of numbers
    for i, num in enumerate(nums):
        #  formula to find the target number
        target_number = target - num
        # Check if the target number is in the dictionary
        if target_number in numbers:
            # if it is, return the indices of two numbers
            return [numbers[target_number], i]
        # else, add the current number and its index to the dictionary
        numbers[num] = i
# Define the function and print the result
result = two_sum(nums, target)
getSum = nums[result[0]] + nums[result[1]]

# Call the function and print the results out
print(f"The indices of the two numbers that add up to {target} are: {result}")
print(f"The sum of the two numbers is: {getSum}")