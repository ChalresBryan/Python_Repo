'''is_palindrome.py'''
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

given a non-empty string
determine if the string is a Palindrome
if so, returl boolean True
if not, return boolen False

Palindrome
-is string
-that is written forward and backwards the same
-single character strings are Palindromes


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
# _recursion
# _iteration

# Time: O(n) | # Space: O(1)
def is_palindrome_iteration(string):

    if len(string) == 1:
        return True

    string_length = len(string)

    for fwd_idx in range(string_length):
        rev_idx = (string_length - 1) - fwd_idx

        if string[fwd_idx] != string[rev_idx]:
            print(f"string[{fwd_idx}]:",string[fwd_idx])
            print(f"string[{rev_idx}]:",string[rev_idx])
            return False

    return True

def is_palindrome__recursion(string, fwd_idx=0, rev_idx=0):
    if fwd_idx >= len(string) - 1:
        return None

    string_length = len(string)

    if string_length == 1:
        return True

    if fwd_idx == 0:
        rev_idx = string_length - 1

    if string[fwd_idx] == string[rev_idx]:
        is_palindrome__recursion(string, fwd_idx + 1, rev_idx - 1)
    else:
        print("string[fwd_idx]:",string[fwd_idx])
        print("string[rev_idx]:",string[rev_idx])
        return False

    return True


string1 = "abcdcba"
string2 = "a"
string3 = "ab"
string4 = "aba"
string5 = "abcdefghihgfeddcba"
print(F"{string1}, isPalindrome:",is_palindrome_iteration(string1))
print(F"{string1}, isPalindrome:",is_palindrome__recursion(string1))
print(" ")
print(F"{string2}, isPalindrome:",is_palindrome_iteration(string2))
print(F"{string2}, isPalindrome:",is_palindrome__recursion(string2))
print(" ")
print(F"{string3}, isPalindrome:",is_palindrome_iteration(string3))
print(F"{string3}, isPalindrome:",is_palindrome__recursion(string3))
print(" ")
print(F"{string4}, isPalindrome:",is_palindrome_iteration(string4))
print(F"{string4}, isPalindrome:",is_palindrome__recursion(string4))
print(" ")
print(F"{string5}, isPalindrome:",is_palindrome_iteration(string5))
print(F"{string5}, isPalindrome:",is_palindrome__recursion(string5))
print(" ")