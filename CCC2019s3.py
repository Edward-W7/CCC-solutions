import random
import copy
array = []
for n in range(3):

    inpt = input().split()
    for i in range(len(inpt)):
        if inpt[i] != 'X':
            inpt[i] = int(inpt[i])
    array.append(inpt)
previous = 0
def fill(arr):
    x = []
    for i in range(3):
        for n in range(3):
            if arr[i][n] == 'X':
                x.append([i, n])
    for i in x:
        row = 0
        colm = 0
        for n in x:
            if i[0] == n[0]:
                row += 1
            if i[1] == n[1]:
                colm += 1
        if row == 1:
            if i[1] == 0:
                arr[i[0]][i[1]] = int(arr[i[0]][1]-(arr[i[0]][2]-arr[i[0]][1]))
            elif i[1] == 1:
                if ((arr[i[0]][0] + arr[i[0]][2])/2).is_integer():
                    arr[i[0]][i[1]] = int((arr[i[0]][0] + arr[i[0]][2])/2)
            elif i[1] == 2:
                arr[i[0]][i[1]] = int(arr[i[0]][1]-(arr[i[0]][0]-arr[i[0]][1]))
        if colm == 1:
            if i[0] == 0:
                arr[i[0]][i[1]] = int(arr[1][i[1]]-(arr[2][i[1]]-arr[1][i[1]]))
            elif i[0] == 1:
                if ((arr[0][i[1]] + arr[2][i[1]])/2).is_integer():
                    arr[i[0]][i[1]] = int((arr[0][i[1]] + arr[2][i[1]])/2)
            elif i[0] == 2:
                arr[i[0]][i[1]] = int(arr[1][i[1]]-(arr[0][i[1]]-arr[1][i[1]]))
    return(arr)

arra = copy.deepcopy(array)
def findx(arry):
    x = []

    for i in range(3):
        for n in range(3):
            if arry[i][n] == 'X':
                x.append([i, n])
    return(x)

def ans(array):


    while (True):
        previous = copy.deepcopy(array)
        array = fill(array)

        if len(findx(array)) == 0:
            for i in array:
                print(*i)

            return(True)
        elif array == previous:
            return(False)
randarr = copy.deepcopy(array)
while(True):

    if ans(randarr):
        break
    else:

        randarr = copy.deepcopy(array)
        x = findx(array)
        randarr[x[random.randint(0, len(x)-1)][0]][x[random.randint(0, len(x)-1)][1]] = random.randint(-1000000, 1000000)


