'''file_name.py'''
# pylint: disable=E1101
print(" ")

A = [1, 2, 3, 5, 6, 8, 9]


def sorted_squared_array(array):
    '''sorted_squared_array'''
    new_array = []

    for num in array:
        new_array.append(num * num)

    return sorted(new_array)

# O(nlog(n)) time | O(n) space


def sorted_squared_array1(array):
    '''sorted_squared_Array'''
    sorted_sqaures = [0 for _ in array]

    for idx, value in enumerate(array):
        sorted_sqaures[idx] = value * value

    sorted_sqaures.sort()
    return sorted_sqaures

# O(n) time | O(n) space


def sorted_squared_array2(array):
    '''sorted_squared_array2'''
    sorted_sqaures = [0 for _ in array]
    smaller_value_idx = 0
    larger_value_idx = len(array) - 1

    for idx in reversed(range(len(array))):
        smaller_value = array[smaller_value_idx]
        larger_value = array[larger_value_idx]

        if abs(smaller_value) > abs(larger_value):
            sorted_sqaures[idx] = smaller_value * smaller_value
            smaller_value_idx += 1

        else:
            sorted_sqaures[idx] = larger_value * larger_value
            larger_value -= 1

    return sorted_sqaures


# O(n^2) time | O(1) space
# O(n) time | O(n) space
# O(nlog(n)) time | O(1) space
print(sorted_squared_array(A))
print(sorted_squared_array1(A))
print(sorted_squared_array2(A))

print(" ")
