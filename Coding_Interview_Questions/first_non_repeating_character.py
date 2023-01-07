'''first_non_repeating_character.py'''
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
    3. Check for no params/empty, 0, undefined, null, massive arrays, async code
    4. Define what/if assumptions can be made about the code

given:
- a string of lowercase english characters

return:
- the index of the given string's first non repeating character

goal:
-find the first character in the string that occurs only once

note:
- return -1 if the given string does not have any non repeating characters

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
def firstNonRepeatingCharacter(string):
    string_length = len(string)
    char_count = {}

    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    for idx in range(string_length):
        char = string[idx]

        if char_count[char] == 1:
            return idx

    return -1

# _recursion
# _iteration


string1 = "abcdcaf"
string2 = "faadabcbbebdf"
string3 = "ababac"
string4 = "a"
string5 = ""
print("string1:", string1)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string1))
print(" ")
print("string2:", string2)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string2))
print(" ")
print("string3:", string3)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string3))
print(" ")
print("string4:", string4)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string4))
print(" ")
print("string5:", string5)
print("firstNonRepeatingCharacter:", firstNonRepeatingCharacter(string5))
print(" ")
