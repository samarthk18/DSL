marklist=[]

def stud_info():
  noofstuds=int(input("Enter number of students:"))
  for i in range(noofstuds):
      marks=int(input("enter marks of student"+str(i+1)+":"))
      marklist.append(marks)
  print(marklist)

def sum():
  sum=0
  count=0
  for i in range(len(marklist)):
      sum=sum+marklist[i]
      count=1+i
      avg=sum/count
  print("sum of marks:", sum)
  print("average marks:", avg)

def max_min():
  min = marklist[0]
  for i in range(len(marklist)):
 
    if marklist[i] < min:
        min = marklist[i] 
 
  print("The smallest element in the list is ",min)
  
  max = marklist[0]
  for i in range(len(marklist)):
 
    if marklist[i] > max:
        max = marklist[i] 
 
  print("The highest element in the list is ",max)

def freq():
  i=0
  x=0
  print("Marks | Frequency")
  for j in marklist:
    if (marklist.index(j)==i):
     print(j, " | ", marklist.count(j))
     if marklist.count(j)>x:
       x=marklist.count(j)
       mark=j
    i=i+1

def absent():
  count = 0
  for i in range(len(marklist)):
    if marklist[i]==0:
      count+=1
      print("Number of students absent for test are: ",count)
    else:
      print("No student is absent")
      
print("Fundamentals of Data Structures")
stud_info()
print("MENU")
print("1.Average score of the class")
print("2.Highest and Lowest score of the class")
print("3.Count of absent students")
print("4.Frequency of marks")

loop='yes'
while loop=='yes':
  ch=int(input("Enter the serial number to compute the above: "))
  if ch==1:
    sum()
  elif ch==2:
    max_min()
  elif ch==3:
    absent()
  elif ch==4:
    freq()
  else:
    print("Enter correct serial number")
