R=int(input("\nEnter the number of rows: ")) #enter number of rows
C=int(input("\nEnter the number of cols: ")) #enter number of columns

matrix1=[]
print("\nEnter the entries rowwise for FIRST matrix: ")

for i in range(R):
  a=[]
  for j in range(C):
    a.append(int(input()))
  matrix1.append(a)
print(matrix1)

matrix2=[]
print("\nEnter the entries rowwise for SECOND matrix: ")

for i in range(R):
  a=[]
  for j in range(C):
    a.append(int(input()))
  matrix2.append(a)
print(matrix2)

result=[]
for i in range(R):
  a=[]
  for j in range(C):
    a.append(0)
  result.append(a)

def add(): #function for addition
  for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
      result[i][j]=matrix1[i][j]+matrix2[i][j]
  print("\nADDITION of matrices is: ",result)

def sub(): #function for subtraction
  for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
      result[i][j]=matrix1[i][j]-matrix2[i][j]
  print("\nSUBTRACTION of matrices is: ",result)

def multi(): #function for multiplication
  for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
      for k in range(len(matrix2)):
        result[i][j]+=matrix1[i][k]*matrix2[k][j]
  print("\nMULTIPLICATION of matrices is: ",result)

def transpose(X): #function for transpose
  for i in range(len(X)):
    for j in range(len(X)):
      result[j][i]=X[i][j]
  print("\nTRANSPOSE of matrix is: ",result)

def main():
  while True:  
    print("\n
    MATRIX OPERATIONS")
    print("\n1.ADDITION")
    print("\n2.SUBTRACTION")
    print("\n3.MULTIPLICATION")
    print("\n4.TRANSPOSE")
    print("\n5.EXIT")
    ch=int(input("\nEnter appropriate serial number for appropriate matrix operation: "))
    if ch==1:
      add()
    elif ch==2:
      sub()
    elif ch==3:
      multi()
    elif ch==4:
      transpose(matrix1)
      transpose(matrix2)
    elif ch==5:
      break
    else:
      print("Invalid operation!")

main()
