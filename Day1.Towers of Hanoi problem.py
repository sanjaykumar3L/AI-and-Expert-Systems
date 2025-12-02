n = int(input())

stack = [(n, "A", "B", "C", 0)]

while stack:
    disks, a, b, c, state = stack.pop()

    if disks == 1:
        print(a, c)
        continue

    if state == 0:
        stack.append((disks, a, b, c, 1))
        stack.append((disks-1, a, c, b, 0))

    else:
        print(a, c)
        stack.append((disks-1, b, a, c, 0))
