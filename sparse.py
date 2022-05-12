def input_matrix(A,r,c):
    print("Enter sparse Matrix ---")
    for i in range(r):
        row=[]
        for j in range(c):
            v=int(input("Enter element : "))
            row.append(v)
        A.append(row)
            
def display_matrix(A,r,c):
    print("Sparse Matrix ---")
    for i in range(r):
        print("\t\t",end=' ')
        for j in range(c):
            print("%3d"%A[i][j],end=' ')
        print("")


def sparse_representation(A,r,c,S):
    triplet_row=[r,c,0]
    count=0
    S.append(triplet_row)
    for i in range(r):
        for j in range(c):
            if(A[i][j]!=0):
                triplet_row=[i,j,A[i][j]]
                S.append(triplet_row)
                count+=1
    S[0][2]=count


def display_sparse_matrix(S):
    print("\t\t-----SPARSE MATRIX------")
    print("\t\t|  Row    Col     Value|")
    print("\t\t|----------------------|")
    print("\t\t|  %3d     %3d      %3d|"%(S[0][0],S[0][1],S[0][2]))
    print("\t\t|----------------------|")
    for i in range(1,S[0][2]+1):
        print("\t\t|  %3d     %3d      %3d|"%(S[i][0],S[i][1],S[i][2]))
    print("")


def simple_transpose(S,T):
    row=[S[0][1], S[0][0], S[0][2]]
    T.append(row)

    for c in range(S[0][1]):
        for j in range(1,S[0][2]+1):
            if(S[j][1]==c):
                row=[ S[j][1], S[j][0], S[j][2] ]
                T.append(row)

def main():
    while True :
      print ("\t Sparse Matrix Operations ")
      print ("\t 1. Input Sparse Matrix as normal")
      print ("\t 2. Display matrix")
      print ("\t 3. Sparse matrix realization ")
      print ("\t 4. Addition of matrix")
      print ("\t 5. Simple Transpose")
      print ("\t 6. Exit")
      ch = int(input("Enter your choice : "))
      if (ch == 6):
         print ("End of Program...")
         quit()
      elif (ch == 1):
          A=[]
          row=int(input("Enter number of rows for sparse matrix : "))
          col=int(input("Enter number of columns for sparse matrix : "))
          input_matrix(A,row,col)

      elif(ch==2):
          display_matrix(A,row,col)

      elif(ch==3):
          S=[]
          sparse_representation(A,row,col,S)
          display_sparse_matrix(S)
     
      elif(ch==5):
          T=[]
          simple_transpose(S,T)
          print("Simple transpose of sparse matrix :")
          display_sparse_matrix(T)
main()     
