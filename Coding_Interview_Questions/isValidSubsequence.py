'''file_name.py'''
# pylint: disable=E1101
print(" ")

S = [1, 1, 1]
A = [1, 1, 1, 1, 1]


def valid_subsequence(array, sequence):
    '''isValidSubsequence'''
    if len(sequence) >= len(array):
        return False

    array_dict = {}
    for num in array:
        if num in array_dict:
            array_dict[num] += 1
        else:
            array_dict[num] = 1

    print(array_dict)

    sequence_dict = {}
    for num in sequence:
        if num in sequence_dict:
            sequence_dict[num] += 1
        else:
            sequence_dict[num] = 1

    print(sequence_dict)

    is_sequence_copy = []

    for num in sequence:
        for num2 in array:
            num_count = sequence_dict.get(num)
            num2_count = array_dict.get(num2)
            if num == num2 and num_count == num2_count:
                is_sequence_copy.append(num)

    print(is_sequence_copy)

    if len(sequence) != len(is_sequence_copy):
        return False

    for i, num in enumerate(sequence):
        if sequence[i] == is_sequence_copy[i]:
            continue

        return False

    return True


# O(n^2) time | O(1) space
# O(n) time | O(n) space
# O(nlog(n)) time | O(1) space


# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    arryIdx = 0
    seqIdx = 0

    while arryIdx < len(array) and seqIdx < len(sequence):
        if array[arryIdx] == sequence[seqIdx]:
            seqIdx += 1

        arryIdx += 1

    return seqIdx == len(sequence)


# O(n) time | O(1) space
def is_valid_subsequence(array, sequence):
    seqIdx = 0

    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1

    return seqIdx == len(sequence)


print(valid_subsequence(A, S))
print(isValidSubsequence(A, S))
print(is_valid_subsequence(A, S))
print(" ")
