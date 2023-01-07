'''semordnilap.py'''
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
- list of unique strings

return:
- a list of semordnilap pairs

notes:
- pair
- different strings
- reverse of one word is the same as the forward version of the other.
- order of strings does not matter

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

def palindrome(words):
    semordnilap_pairs = []
    words_length = len(words)
    store_idxs = {}

    for current_idx in range(words_length):
        word = words[current_idx]
        word_length = len(word)

        for iterator in range(words_length):
            palindrome = words[iterator]
            palindrome_length = len(palindrome)

            if word_length == palindrome_length and current_idx != iterator:
                if word == palindrome[::-1]:
                    if current_idx not in store_idxs:
                        if iterator not in store_idxs:
                            semordnilap_pairs.append(tuple((word, palindrome)))
                            store_idxs[current_idx] = store_idxs.get(current_idx, 0) + 1
                            store_idxs[iterator] = store_idxs.get(iterator, 0) + 1

    return semordnilap_pairs

def semordnilap(words):
    semordnilap_pairs = []
    words_length = len(words)
    words_dict = {}

    for current_idx in range(words_length):
        word = words[current_idx]
        words_dict[word] = current_idx

    for current_idx in range(words_length):
        word = words[current_idx]
        palindrome = word[::-1]

        if palindrome in words_dict:
            palindrome_idx = words_dict[palindrome]

            if current_idx != palindrome_idx:
                semordnilap_pairs.append(tuple((word, palindrome)))
                words_dict.pop(word)

    return semordnilap_pairs

words1 = ["abcde", "edcba", "edbc", "edb", "cbde", "abc"]
print("words1:",words1)
print("palindrome:",palindrome(words1))
print("semordnilap:",semordnilap(words1))
print(" ")
words2 = ["aaa", "bbbb"]
print("words2:",words2)
print("palindrome:",palindrome(words2))
print("semordnilap:",semordnilap(words2))
print(" ")
words3 = ["dog", "god"]
print("words3",words3)
print("palindrome:",palindrome(words3))
print("semordnilap:",semordnilap(words3))
print(" ")

# _recursion
# _iteration
print(" ")