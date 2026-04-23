
def pascal_triangle(nRows):
    triangle = []

    for row in range(nRows):
        if row == 0:
            triangle.append([1])
        else:
            newRow = [1]
            prevRow = triangle[row - 1]

            for j in range(1, row):
                newRow.append(prevRow[j - 1] + prevRow[j])
            
            newRow.append(1)
            triangle.append(newRow)
        return triangle

print(pascal_triangle(10))


