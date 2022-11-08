tests = int(input())
for _ in range(tests):
    n = int(input())
    stack = []
    needed = 1
    currlst = []
    for i in range(n):
        currlst.append(int(input()))
    for i in range(n):
        curr = currlst[n-i-1]
        if curr == needed:
            needed += 1
        else:
            stack.append(curr)
        if not stack:
            pass
        elif stack[-1] == needed:
            stack.pop()
            needed += 1
        while stack:

            if stack[-1] == needed:
                needed += 1
                stack.pop()
            else:
                break
    while stack:

        if stack[-1] == needed:
            needed += 1
            stack.pop()
        else:
            break
    if not stack:
        print("Y")
    else:
        print("N")

