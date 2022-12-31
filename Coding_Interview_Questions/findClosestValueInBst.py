'''findClosestValueInBst.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

# assume that there is only one closet value

# O(1) time | O(1) space


def findClosestValueInBst(tree, target):
    # Write your code here.
    closest_value = None
    smallest_abs_difference = None
    current = tree

    while current is not None:

        if current.value == target:
            closest_value = current.value
            break

        if target < current.value:
            if smallest_abs_difference > abs(current.value - target):
                closest_value = current.value

            current = current.left

        else:
            if smallest_abs_difference > abs(current.value - target):
                closest_value = current.value

            current = current.right

    return closest_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


print(" ")
