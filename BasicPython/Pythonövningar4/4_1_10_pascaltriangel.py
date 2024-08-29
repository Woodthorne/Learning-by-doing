n = int(input('Hur många rader av Pascals Triangel? '))
triangle = []
for step in range(n):
    row = [1]
    if step > 1:
        for value in range(1,len(triangle[step-1])):
            row.append(triangle[step-1][value-1]+triangle[step-1][value])
    if step > 0:
        row.append(1)
    triangle.append(row)
    print(row)