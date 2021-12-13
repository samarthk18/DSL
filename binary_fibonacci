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
        

def iterative_binary_search(A, n, key):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(A[mid]==key):
            return mid        #key found
        elif(key<A[mid]):
            high=mid-1
        else:
            low=mid+1

    return -1                 #not found
        

def recursive_binary_search(A,low,high,key):
    if(low<=high):
        mid=(low+high)//2
        if(A[mid]==key):
            return mid     #found key
        elif(key < A[mid]):
            return recursive_binary_search(A,low,mid-1,key)
        else:
            return recursive_binary_search(A,mid+1,high,key)

    return -1        #Key NOT FOUND 
            

def fibonacci_search(A, n, key):
    f1=0
    f2=1
    f3=f1+f2
    offset=-1
    while(f3 < n):
        f1=f2
        f2=f3
        f3=f1+f2

    while(k>1):
        i=min(offset+f1, n-1)

        if(key == A[i]):
            return i         #found key at i

        elif(key > A[i]):    # right substudent ( 33 % or 1/3 student)
            f3=f2
            f2=f1
            f1=f3-f2
            offset=i
        else:			# left substudent (66 % or 2/3 student)
            f3=f1
            f2=f2-f3       #f1=f2-f1
            f1=f3-f2

    if(f2==1 and A[offset+1]==key ): #comparing the last element with key
        return offset+1      #key found 
    
    return -1
            
     
            
     
  
def main():
    while True:
       print("\n\n")
       print("\t1: Accept students who attended training program ")
       print("\t2: Display students who attended training program ")
       print("\t3: Binary  Iterative Search")
       print("\t4: Binary  Recursion Search")
       print("\t5: Fibonacci Search")
       print("\t6: Exit")
       ch=int(input("\t Enter Your Choice : "))
       if ( ch==6 ):
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
           n=len(stud_arr)
           x=iterative_binary_search(stud_arr, n, key)
           if(x == -1):
               print("\t Student not attending training program ")
           else:
               print("\t Student attended training , present at location  ",(x+1))

       elif(ch==4):
           key=int(input("\t Enter roll number to be search :"))
           x=recursive_binary_search(stud_arr, 0,len(stud_arr)-1, key)
           if(x == -1):
               print("\t Student not attending training program ")
           else:
               print("\t Student attended training , present at location  ",(x+1))
              
       elif(ch==5):
           key=int(input("\t Enter roll number to be search :"))
           n=len(stud_arr)
           x=fibonacci_search(stud_arr, n, key)
           if(x == -1):
               print("\t Student not attending training program ")
           else:
               print("\t Student attended training , present at location ",(x+1))
       else:
           print("INVALID CHOICE")

main()
