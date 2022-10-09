#this solution uses a random number generator, and may not ac all of the time
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

def findx(array):
    x = []
    for i in range(3):
        for n in range(3):
            if array[i][n] == 'X':
                x.append([i, n])
    return(x)
def findnum(array):
    num = []
    for i in range(3):
        for n in range(3):
            if array[i][n] != 'X':
                num.append([i, n])
    return(num)
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
num = findnum(array)


if len(num) == 2:

    num1 = array[num[0][0]][num[0][1]]
    num2 = array[num[1][0]][num[1][1]]

    if num[0][0] != num[1][0]:
        if num[0][0] == 0 and num[1][0] == 1:
            array = [[num1]*3, [num2]*3, [num2-(num1-num2)]*3]
        elif num[0][0] == 1 and num[1][0] == 2:
            array = [[num1-(num2-num1)] * 3, [num1] * 3, [num2]*3]
        elif num[0][0] == 0 and num[1][0] == 2:
            array = [[num1] * 3, [int((num1+num2)/2)] * 3, [num2] * 3]
    elif num[0][0] == num[1][0]:
        if num[0][1] == 0 and num[1][1] == 1:
            array = [[num1, num2, num2-(num1-num2)], [num1, num2, num2-(num1-num2)], [num1, num2, num2-(num1-num2)]]
        elif num[0][1] == 1 and num[1][1] == 2:
            array = [[num1-(num2-num1), num1, num2], [num1-(num2-num1), num1, num2], [num1-(num2-num1), num1, num2]]
        elif num[0][1] == 0 and num[1][1] == 2:
            array = [[num1, int((num1+num2)/2), num2], [num1, int((num1+num2)/2), num2], [num1, int((num1+num2)/2), num2]]
    for i in array:
        print(*i)
elif len(num) == 1:
    num1 = array[num[0][0]][num[0][1]]
    array = [[num1] * 3, [num1] * 3, [num1] * 3]
    for i in array:
        print(*i)
elif len(num) == 0:
    print("0 0 0")
    print("0 0 0")
    print("0 0 0")
else:
    while(True):
        if ans(randarr):
            break
        else:
            randarr = copy.deepcopy(array)
            x = findx(array)
            randarr[x[random.randint(0, len(x)-1)][0]][x[random.randint(0, len(x)-1)][1]] = random.randint(-100000, 100000)

