from typing import List

# first given list
l1 = [2,4,3]
# second given list
l2 = [5,6,4]
# target sum to find:
target = 807

# function to add two numbers represented as linked lists
def addTwoNumbers(l1: List[int], l2: List[int]) -> List[int]:

    # Reverse the input lists to the correct order
    new_list1 = l1[::-1]
    new_list2 = l2[::-1]

    # join the numbers in the list to form a single number
    num1 = int(''.join(map(str, new_list1)))
    num2 = int(''.join(map(str, new_list2)))
    # Calculate the sum of the two numbers
    total = num1 + num2
    # Call the function and print the result out
    print(f"The sum of the two digits is: {total}")

# Give the function the two lists and print the result out
addTwoNumbers(l1, l2)
    