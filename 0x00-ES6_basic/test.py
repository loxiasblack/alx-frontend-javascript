#!/usr/bin/python3

if __name__ == "__main__":
    
    n = 6
    pascal_triangle = []
    
    for i in range(n):
        row = []
        if i == 0:
            row.append(1)
        for j in range(i):
            if j > 0 and j < len(pascal_triangle[i - 1]):
                n = pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j - 1]
                row.append(n)
            else:
                row.append(1)
        if i > 0 and len(row) == len(pascal_triangle[i - 1]):
            row.append(1)
        pascal_triangle.append(row)
        
    for list in pascal_triangle:
        print(list)


    def canUnlockAll(boxes):
        keys = {0}
        open = set()
        while keys - open:
            current = (keys - open).pop()
            open.add(current)
            for key in boxes[current]:
                keys.add(key)
        
        return len(open) == len(boxes)

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
