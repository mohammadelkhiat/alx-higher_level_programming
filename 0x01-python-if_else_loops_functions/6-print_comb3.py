#!/usr/bin/python3
for i in range(0, 10):
    for n in range(i, 10):
        if i != n:
            if i < 8 or n < 9:
                print('{}{}'.format(i, n), end=', ')
            else:
                print('{}{}'.format(i, n))
