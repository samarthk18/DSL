cricket=[]
badminton=[]
football=[]
universal=[]
def stud_info(x,Str):
  noofstuds=int(input("Enter the total no. of student who play %s : "%Str))
  for i in range(noofstuds):
      players=input("Enter name of the student %s :"%Str)
      x.append(players)
      if players not in universal:
        universal.append(players)
  print("Set of students playing %s "%Str,x)

stud_info(cricket,"cricket")
stud_info(badminton,"badminton")
stud_info(football,"football")

def first():
  U = []
  for i in cricket:
    for j in badminton:
      if i == j:
        U.append(i)
  print("\nList of students who play both cricket and badminton are:",U)

def second():
  V=[]
  for i in cricket:
    if i not in badminton:
      V.append(i)
  for j in badminton:
    if j not in cricket:
      V.append(j)     
  print("\nList of students who play either cricket or badminton but not both are:",V)

def third():
  X=[]
  Y=[]
  for i in cricket:
    X.append(i)

  for j in badminton:
    if j not in X:
      X.append(j)
  
  for k in universal:
    if k not in X:
      Y.append(k)
  print("\nList of students who play neither cricket nor badminton.",Y)
  print("\nNumber of students who play neither cricket nor badminton.",len(Y))
 
def fourth():
  a=[]
  for i in cricket:
    a.append(i)
  for j in football:
    if j not in a:
      a.append(j)
  for k in badminton:
    if k in a:
      a.remove(k)
  print("\nList of students who play Cricket and Football but not badminton",a)
  print("\nNumber of students who play Cricket and Football but not badminton",len(a))

def main():
    while True:
        print("\n1. List the students who play both cricket and badminton")
        print("\n2. List the students who play either cricket or badminton but not both")
        print("\n3. Number of students who play neither cricket nor badminton")
        print("\n4. Number of students who play Cricket and Football but not badminton")
        print("\n5. Exit")
        print("\nEnter Your Choice")
        choice=int(input())
        if choice==1:
          first()
        elif choice==2:
          second()
        elif choice==3:
          third()
        elif choice==4:
          fourth()
        elif choice==5:
              break

main()
