b = [10.1, 9.7, 7.8]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i != j:
            matrix[i][j] = -matrix[i][j] / matrix[i][i]
    b[i] = - b[i] / matrix[i][i]
    matrix[i][i] = 0
    
for i in range(len(matrix)):
    print(matrix[i])
    
print(b)


x0 = [0] * len(matrix)
x1 = [0] * len(matrix)
x = [[0] * len(matrix)] * len(matrix)
print(x)

for counter in range(len(matrix) - 1):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            x[counter + 1][i] += x[counter][j] * matrix[i][j]
        x[counter + 1][i] += b[i] 

print(x)
