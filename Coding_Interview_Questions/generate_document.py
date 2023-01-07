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

givens:
-a string of available characters
-a string of the document that needs to be generated

return boolen True if you can create the document using the available characters
return boolen False if you can not create the document using the avaiable characters

Note:
-if the frequency of unique characters matters
-all characters can be inside the input
-empty string can always be generated

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


# Time: O(n + m) | # Space: O(n)
def generateDocument(characters, document):
    if document == "":
        return True

    available_chars = {}

    for char in characters:
        if char in available_chars:
            available_chars[char] += 1
        else:
            available_chars[char] = 1

    print(available_chars)

    for char in document:
        if char in available_chars:
            available_chars[char] -= 1
            if available_chars.get(char) < 0:
                return False
        else:
            print(available_chars)
            return False

    return True


characters1 = "Bste!hetsi ogEAxpelrt x "
document1 = "AlgoExpert is the Best!"
print(generateDocument(characters1, document1))
print(" ")
characters2 = "aheaolabbhb"
document2 = "hello"
print(generateDocument(characters2, document2))
print(" ")

# _recursion
# _iteration
print(" ")
