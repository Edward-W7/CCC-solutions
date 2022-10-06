quer = [i for i in input()]
if quer.count('H') % 2 == 0:
    if quer.count('V') % 2 == 0:
        print("1 2")
        print( "3 4")
    else:
        print("2 1")
        print( "4 3")
else:
    if quer.count('V') % 2 == 0:
        print("3 4")
        print("1 2")

    else:
        print("4 3")
        print("2 1")
