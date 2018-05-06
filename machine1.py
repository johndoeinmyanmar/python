def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def linear_search(A,num):
    mid = len(A) // 2
    if num == A[mid]:
        print('found')
        return num
    elif num > A[mid]:
        print('larger')
        return linear_search(A[mid+1:],num)
    else:
        print('smaller')
        return linear_search(A[:mid],num)
        

def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length -1)
        draw_line(center_length)
        draw_interval(center_length -1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1,1+num_inches):
        draw_interval(major_length -1)
        draw_line(major_length, str(j))

import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:<7}'.format(total), path)
    return total

def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

def reverse(S, start, stop):
    if start < stop-1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)


num = list(range(100))
reverse(num, 0, 100)
