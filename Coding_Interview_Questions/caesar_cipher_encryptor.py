'''file_name'''
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

given
-a non empty string of lowercase characters
and
-a non negative integer represeting a key

return a new string
-shift every character "k" postions

note:
characters should wrap if they pass z


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

# Time: O(n) | # Space: O(n)
def caesarCipherEncryptor(string, key):
    shifted_string = ''
    first_char_Unicode = ord("a")
    last_char_Unicode = ord("z")
    key = key % 26
    wrap_char = last_char_Unicode - first_char_Unicode + 1

    for char in string:
        if ord(char) + key > last_char_Unicode:
            shifted_char = ord(char) + key - wrap_char
            shifted_string += chr(shifted_char)
        else:
            shifted_char = ord(char) + key
            shifted_string += chr(shifted_char)

    return shifted_string


string1 = "xyz"
key1 = 2
print(F"String1: {string1}")
print(F"key1: {key1}")
print("after:",caesarCipherEncryptor(string1,key1))
print(" ")
string2 = "abc"
key2 = 0
print(F"String2: {string2}")
print(F"key2: {key2}")
print("after:",caesarCipherEncryptor(string2,key2))
print(" ")
string3 = "abc"
key3 = 3
print(F"string3: {string3}")
print(F"key3: {key1}")
print("after:",caesarCipherEncryptor(string3,key3))
print(" ")


# _recursion
# _iteration
print(" ")