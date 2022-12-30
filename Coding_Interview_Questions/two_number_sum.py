'''two_number_sum.py'''
# pylint: disable=E1101
print(" ")

# O(n^2) time | O(1) space
def two_number_sum(array, target_sum):
    '''two_number_sum'''

    for i, num in enumerate(array):
        for i_i, num2 in enumerate(array):
            if i == i_i:
                continue

            if num + num2 == target_sum:
                return [num, num2]

    return []

# O(n) time | O(n) space
def twoNumberSum2(array, targetSum):
    '''twoNumberSum2'''

    nums = {}
    
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return[potentialMatch, num]
        else:
            nums[num] = True

    return []


# O(nlog(n)) time | O(1) space
def twoNumberSum3(array, targetSum):
    '''twoNumberSum3'''

    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == targetSum:
            return [array[left], array[right]]
        elif current_sum < targetSum:
            left += 1
        elif current_sum > targetSum:
            right -= 1

    return []

print(" ")
