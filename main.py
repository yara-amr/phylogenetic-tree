#Merna Hesham Mahmoud
#Haidy Kamal Makram
#Yara Amr Ahmed
#Maram Nasser
#Maram Hatem
#Yasmine Mohamed El-Gazar




import numpy as np

Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

def matrix_name(beginning, end):
    names = []
    for i in range(ord(beginning), ord(end) + 1):
        names.append(chr(i))
    print(names)
    return names

first = (input("Enter the name of first row:"))
last = (input("Enter the name of last row:"))
m_name = matrix_name(first,last)

print("Enter the values in a single line (separated by space): ")
values = list(map(float, input().split()))
matrix = np.array(values).reshape(Row, Column)
print(matrix)


def Minimum(matrix):
    min = 10000
    global x
    global y
    for i in range(Row):
        for j in range(Column):
            if i != j:
                if min > matrix[i][j]:
                    min = matrix[i][j]
                    x = i
                    y = j

    print("minimum is:", min)
    print("index:", x, " ", y)
    return x, y


def cluster(names, x,y):
    print(matrix)
    if y < x:
        x, y =y, x
    names[x] = "(" + names[x] + "," + names[y] +")"
    del names[y]


def updatematrix(matrix, x, y):

      for i in range(1,len(matrix[0])):
        if (i > y):
            matrix[x][i] = (matrix[x][i] + matrix[y][i])/2
            matrix = np.delete(matrix, (x+1), 0)
            matrix = np.delete(matrix, y, 1)

      print(matrix)


def phylo_tree(matrix, names):
    while len(names) > 1:
        x, y = Minimum(matrix)
        updatematrix(matrix, x, y)
        cluster(names, x, y)
    return names[0]


tree = phylo_tree(matrix,m_name)
print(tree)

