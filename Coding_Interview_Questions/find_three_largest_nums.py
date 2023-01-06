'''find_three_largest_nums.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
print(" ")

'''
1. Write down the key points of the question

given an array of three or more integers
without sorting the array
return a sorted array of the three largest integers

return duplicate integers if necessary

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

# Time: O(n) | # Space: O(1)


def findThreeLargestNumbers(array):
    three_largest_nums = [-999999999, -999999999, -999999999]

    for num in array:
        min_large_num = min(three_largest_nums)

        for idx, large_num in enumerate(three_largest_nums):
            if large_num == min_large_num:
                if num > min_large_num:
                    three_largest_nums[idx] = num
                break

        three_largest_nums.sort()

    return three_largest_nums


arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(arr))
print(" ")
