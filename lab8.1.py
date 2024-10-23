from array import *

arr = array('i', [])
for i in range(12):
    arr.append(i + 1)

print(arr)

j = 0
for i in range(len(arr)):
    if(i % 2 == 0):
        arr[i] = 10**j
        j += 1

print(arr)

arr.pop(0)
arr.pop(-1)

print(arr)