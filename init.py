matrix = [[7.6, 5.8, 4.7], [3.8, 4.1, 2.7], [2.9, 2.1, 3.8]]
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
x = [[0] * len(matrix)] * 2
print(x[1][2])

for counter in range(2):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            x[counter + 1][i] += x[counter][j] * matrix[i][j]
        x[counter + 1][i] += b[i] 

print(x)
