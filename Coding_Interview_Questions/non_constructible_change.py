'''non_constructible_change.py'''
# pylint: disable=E1101
print(" ")

# array of values
# find the minimum sum of values that cannot be created
# coins can not reused to make new value

coins1 = []
coins2 = [1, 2, 5]
coins3 = [5, 7, 1, 1, 2, 3, 22]

# find n > sum + 1
# where n is a value in an array

# O(nlog(n)) time | O(1) space


def non_constructible_change(coins):
    '''non_constructible_change'''
    if len(coins) == 0:
        return 1

    coins.sort()
    current_sum = 0

    for coin in coins:
        if coin > current_sum + 1:
            return current_sum + 1

        current_sum += coin

    return current_sum + 1


print(non_constructible_change(coins1))
print(non_constructible_change(coins2))
print(non_constructible_change(coins3))

print(" ")
