'''selection_sort.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
1. Write down the key points of the question.
    1. Input (no assumptions)
        1. check for false inputs that you don't want
    2. Output (no assumptions)
        1. check for false outputs that you don't want
    3. Check for no params, 0, undefined, null, massive arrays, async code
    4. Define what/if assumptions can be made about the code

given an array of integers
return the given array sorted

2. What is more valuable? Time or Space?

3. Start with the naive/brute force approach.
    1. The first thing that comes into mind.
    2. Just speak about it
    3. Tell them why this approach is not the best.

4. Find a new solution with the answer to question 2 in mind.
    1. Did you use all the given information?
    2. Focus on the part of the code with the biggest Big O

5. Before you start coding, walk and write down the steps
    1. Modularize your code
    2. write tests now to make your function fail

6. Once the comments are written, start actually writing your code now.
    1. remember punctuation and imports

7. Finally, talk to the interviewer where you would improve the code.
    1. Does it work?
    2. Are there different approaches?
    3. Is it readable?
    4. What would you google to improve?
    5. How can performance be improved?
    6. Scale of input
        1. divide-and-conquer approach / distributed processing of the data
            1. divide and read parts of input from disk into memory
            2. write the output back to disk and combine them later.
'''

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Time: O(n^2) | # Space: O(1)
def selectionSort(array):
    # for any given index, iterate from the index to the end of the array.
    # find the smallest num
    # swap the given index value with he smallest num
    
    for i in range(0,len(array)-1):
        j = i
        num = array[j]
        smallest_num = array[j]
        found_swap = False

        while j < len(array)-1:
            j += 1
            num = array[j]
            if num < smallest_num:
                smallest_num_index = j
                smallest_num = num
                found_swap = True

        if found_swap is True:
            swap(i, smallest_num_index, array)

    return array


arr = [1, 2]
print("before:",arr)
print("after:",selectionSort(arr))
print(" ")