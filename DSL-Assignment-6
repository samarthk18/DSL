def accept_Rollno(A):
    n=int(input("\t Enter number of students who attended training :"))
    print("\t Enter rollnumber of students : ")
    for i in range(n):
        x=int(input("\t Enter roll number : "))
        A.append(x)

def display(A,n):
    if(n==0):
        print("\t No student have attended training program ")
    else:
        
        print("\t List of students attended tarining program :")
        for i in range(n):
            print(A[i],end="  ")
    print("")
        

def linear_search(A, n, key):
    for i in range(n):
        if(A[i]==key):
            return i                #roll no found at i
    return -1                       #Not found
        

def sentinal_search(A, n, key):
    last=A[n-1]
    A[n-1]=key

    i=0
    while(A[i]!=key):
        i=i+1
        
    A[n-1]=last
    if( (i<n-1) or (key==last) ):
        return i       #roll no found at i
    else:
        return -1      #Not found
    
    
def main():
    while True:
       print("\t1: Accept students who attended training program ")
       print("\t2: Display students who attended training program ")
       print("\t3: Linear Search")
       print("\t4: Sentinal Search")
       print("\t5: Exit")
       ch=int(input("\t Enter Your Choice : "))
       if ( ch==5 ):
           print("\t End of Program!")
           quit()
       elif(ch==1):
           stud_arr=[]
           accept_Rollno(stud_arr)

       elif(ch==2):
           n=len(stud_arr)
           display(stud_arr,n)

       elif(ch==3):
           key=int(input("\t Enter roll number to be search :"))
           x=linear_search(stud_arr, n, key)
           if(x == -1):
               print("\t Student not attending training program ")
           else:
               print("\t Student attended training , present at location %d "%(x+1))

       elif(ch==4):
           key=int(input("\t Enter roll number to be search :"))
           x=sentinal_search(stud_arr, n, key)
           if(x == -1):
               print("\t Student not attending training program ")
           else:
               print("\t Student attended training , present at location %d "%(x+1))
           
      else:
          print(" Invalid choice !!!")
main()
