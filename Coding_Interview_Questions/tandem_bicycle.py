'''tandem_bicycle.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

a = [1, 
     3, 
     5, 1, 4, 
     6, 2, 4]

q = int(input())
n = int(input())
dmoj = list(map(lambda x: int(x), input().split(" ")))
peg = list(map(lambda x: int(x), input().split(" ")))

speed = 0
dmoj.sort() # min - max
peg.sort() # min - max
if q == 1:
    # min total speed
    for i in range(n):
        speed += max(dmoj[i], peg[i])

else:
    # max total speed
    dmoj = dmoj[::-1]
    for i in range(n):
        speed += max(dmoj[i], peg[i])

print(speed)

print(" ")
