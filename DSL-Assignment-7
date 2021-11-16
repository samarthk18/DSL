students_per=[]
n=int(input("Enter number of students: "))
for i in range(n):
  students_per.append(float(input("Enter Percentage: ")))

def bubble():
  for i in range(n):
    for j in range(0, n-i-1):
      if students_per[j] > students_per[j+1]:
        students_per[j],students_per[j+1]=students_per[j+1],students_per[j]
  print("Bubble sort ",students_per[0:5])

bubble()

def selection():
  for i in range(len(students_per)):
    min=i
    for j in range(i+1,len(students_per)):
      if students_per[min]>students_per[j]:
        min=students_per[i]
        min=j
        students_per[i],students_per[min]=students_per[min],students_per[i]
selection()
print("Selection sort ",students_per)
