
# r = row number
#   1     (r = 1)
# 1 2 1   (r = 2)
# 1 3 3 1 (r = 3)
# ...

# Number of Space, printed value, Number of Space
# if r = 2,
# for the first row, print r - 1 spaces, rCn, r-1 spaces
# for the second row, print r-2 spaces, rCn, r-2 spaces
# for the third row, print r - 3 spaces, rCn, rCn, r-3 spaces ... (space formula = r - iteration)


#code

# r = int(input('row = '))
#
# if (r > 0):
#
# else:


def combination(r, i):
    cv = r
    cv2 = i
    if (i == 0 | i == r):
        return (1)
    for counter in range (1, i):
        cv = cv * (r - counter)
        if (i == 1):
            return (cv)
        else:
            cv2 = cv2 * (i - counter)
            return (int(cv / cv2))

print(combination(6,3))

import math
r = int(input("r = ?"))

for n in range(r):
    for k in range(r):
        if k <= n:
            print(f"{math.comb(n, k):3}", end=" ")
        else:
            print("   ", end=" ")
    print()




