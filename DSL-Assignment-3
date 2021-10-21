R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
matrix1 = [] 
print("Enter the entries rowwise for first matrix:") 
   
for i in range(R):          
    a =[] 
    for j in range(C):      
         a.append(int(input())) 
    matrix1.append(a) 
print(matrix1) 
  

matrix2 = [] 
print("Enter the entries rowwise for second matrix:") 
   
for i in range(R):          
    a =[] 
    for j in range(C):      
         a.append(int(input())) 
    matrix2.append(a) 
print(matrix2)


result = []
for i in range(R):          
    a =[] 
    for j in range(C):      
         a.append(0) 
    result.append(a) 

for i in range(len(matrix1)):  
    for j in range(len(matrix2[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print("Addition of matrices is: ",result)

for i in range(len(matrix1)):  
    for j in range(len(matrix2[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
print("Subtraction of matrices is: ",result)

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
print("Multiplication of matrices is: ",result)

def transpose(X):
  for i in range(len(X)):
    for j in range(len(X[0])):
       result[j][i] = X[i][j]
  print("Transpose of matrix is ",result)

transpose(matrix1)
transpose(matrix2)
