Метод постых итераций.

1 шаг. Преобразовываем матрицу методом Якоби.

2 шаг. Берем за начальное приближение нулевой вектор.

3 шаг. По МПИ находим более точное приближение.

import copy
import math
from numpy import linalg as LA
#matrix = [[7.6, 5.8, 4.7], [3.8, 4.1, 2.7], [2.9, 2.1, 3.8]]
#b = [10.1, 9.7, 7.8]


matrix = [[1.1, -0.2, 0.1], [0.1, -1.2, -0.2], [0.2, -0.1, 1.1]]
b = [-1.6, -2.3, -1.5]

#matrix = [[34, 2, -1], [3.4, -8, -7], [0.8, 1.3, 5]]
#b = [-1.9, 2.4, -1.2]

matrix_test = copy.deepcopy(matrix)
b_test = copy.deepcopy(b)

def multiplying_I(x, b, matrix): #нахождение і-го приближения
    a = copy.deepcopy(x)
    for i in range(len(matrix)):
        x[i] = a[0] * matrix[i][0]
        for j in range(1, len(matrix)):
            x[i] += a[j] * matrix[i][j]
        x[i] += b[i]
    return(x)



def norm_matrix(matrix): #нахождение кубической нормы матрицы
    max = 0
    for i in range(len(matrix)):
        norm_matrix = 0
        for j in range(len(matrix)):
            norm_matrix += math.fabs(matrix[i][j])
        if norm_matrix > max:
            max = norm_matrix
    return max


#функции вывода на экран
def print_vector(b, n):
    for i in range(len(b)):
        print('{:>6}'.format(round(b[i], n).__str__()), end=' ')
    print("\n")
    
    

#функции вывода на экран
def print_matrix(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print('{:>6}'.format(round(matrix[i][j], n).__str__()), end=' ')
        print("\n")
    
print(" ")
print("Данная матрица А")
print_matrix(matrix, 3)

print(" ")
print("Вектор свободных членов")
print_vector(b, 3)
print(" ")

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i != j:
            matrix[i][j] = -matrix[i][j] / matrix[i][i]
    b[i] = - b[i] / matrix[i][i]
    matrix[i][i] = 0
print(" ")
print("Преобразованная матрица А")    
print_matrix(matrix, 3)
print(" ")
print("Преобразованный вектор свободных членов")
print_vector(b, 3)
print(" ")
#print(LA.eig(matrix))

x = [float(0)]* len(matrix)
#x = float(x)
print(x)

norm = norm_matrix(matrix)
count = 0
eps = 1
    
while math.fabs(eps) >= 0.001 and count < 30:
    old_x = copy.deepcopy(x)
    x = multiplying_I(x, b, matrix)
    count = count + 1
    print(" ")
    print(count, "шаг")
    print_vector(x, 8)
    norm_x = 0
    for i in range(len(x)):
        if math.fabs(x[i]-old_x[i]) > norm_x:
            norm_x = math.fabs(x[i]-old_x[i])
    eps = norm*(norm_x)/(1 - norm)
    
    norm_x0x1 = 0
    for i in range(len(x)):
        if math.fabs(b[i]) > norm_x0x1:
            norm_x0x1 = math.fabs(b[i])           
    norm_x = (norm ** (count + 1))*(norm_x0x1) / (1 - norm)
    print("априорная погрешность =", norm_x)
    print("апостериорная погрешность =", eps)
           
    
if math.fabs(eps) < 0.001:
    print(" ")
    print("Метод простых итераций сходится за ",count, "шагов")
    print("вектор решения:")
    for i in range(len(x)):
        print("x[",i + 1,"] =",round(x[i], 3))
else:
    print(" ")
    print("метод простых итераций расходится")
    

    
    #нахождение вектора невязки
if math.fabs(eps) < 0.001:
    r = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            r[i] += matrix_test[i][j] * x[j]
        r[i] += b_test[i]
        r[i] = round(math.fabs(r[i]), 3)
    print("вектор невязки")    
    print_vector(r, 3)
    
    def multiplying_Z(x, b, matrix):
    for i in range(len(matrix)):
        x[i] = x[0] * matrix[i][0]
        for j in range(1, len(matrix)):
            x[i] += x[j] * matrix[i][j]
        x[i] += b[i]    

    return(x)

 

print(" ")
print("Преобразованная матрица А")    
print_matrix(matrix, 3)
print(" ")
print("Преобразованный вектор свободных членов")
print_vector(b, 3)
print(" ")


x = [float(0)]* len(matrix)
x[0] = b[0]

count = 0
eps = 1
    
while math.fabs(eps) >= 0.00001 and count < 30:
    old_x = copy.deepcopy(x)
    x = multiplying_Z(x, b, matrix)
    count = count + 1
    print(" ")
    print(count, "шаг")
    print_vector(x, 8)
    norm_x = 0
    for i in range(len(x)):
        if math.fabs(x[i]-old_x[i]) > norm_x:
            norm_x = math.fabs(x[i]-old_x[i])
    eps = (norm ** (count + 1))*(norm_x)/(1 - norm)
    apr = 0
    for i in range(len(x)):
        if math.fabs(x[i]) > apr:
            apr = math.fabs(x[i])
    apr = (norm ** (count + 1))*(apr)/(1 - norm)
    print("априорная погрешность =", apr)
    print("апостериорная погрешность =", eps)
           
    
if math.fabs(eps) < 0.001:
    print(" ")
    print("Метод Зейделя сходится за ",count, "шагов")
    print("вектор решения:")
    for i in range(len(x)):
        print("x[",i + 1,"] =",round(x[i], 3))
else:
    print(" ")
    print("метод Зейделя расходится")
    
    
#нахождение вектора невязки
if math.fabs(eps) < 0.001:
    r = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            r[i] += matrix_test[i][j] * x[j]
        r[i] += b_test[i]
        r[i] = round(math.fabs(r[i]), 3)

    print("вектор невязки")    
    print_vector(r, 3)
    
