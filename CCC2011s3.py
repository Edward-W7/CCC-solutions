cases = int(input())


def quad(mag, x, y):
    return [(x) // (5 ** (mag-1)), (y) // (5 ** (mag-1))]


def find(mag, x, y):
    if mag == 1:
        if [x, y] in [[1, 0], [2, 0], [3, 0], [2, 1]]:
            return 'crystal'
        else:
            return 'empty'
    else:
     #   print(mag, x, y)
       # print(quad(mag, x, y))
        if quad(mag, x, y) in [[1, 0], [2, 0], [3, 0], [2, 1]]:
            return 'crystal'
        elif quad(mag, x, y) in [[1, 1], [2, 2], [3, 1]]:
            return find(mag - 1, x - quad(mag, x, y)[0] * (5**(mag-1)), y - quad(mag, x, y)[1] * (5**(mag-1)))
        else:
            return 'empty'

for _ in range(cases):
    mag, x, y = map(int, input().split())

    print(find(mag, x, y))
