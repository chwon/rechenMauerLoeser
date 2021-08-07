# RechenMauerLoeser
#
# Given an array of integers (the base line),
# the code calculates a pyramid of integers, where
# each number is the sum of the two integers
# situated one line below.


base_line = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]

pyramid = [base_line]
half_indent = 5

for i in range(len(base_line)-1):
    arr = []
    for j in range(len(base_line)-(i+1)):
        arr.append(pyramid[i][j] + pyramid[i][j+1])
    pyramid.append(arr)

for i in reversed(range(len(base_line))):
    indent = half_indent * i
    print("".rjust(indent), end='')
    for j in range(len(pyramid[i])):
        print(str(pyramid[i][j]).rjust(half_indent * 2), end='')
    print()

