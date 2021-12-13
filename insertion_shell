def insertion(array):
  for i in range(len(array)):
    temp=array[i]
    for j in range(i+1,len(array)):
      if temp>array[j]:
        array[i],array[j]=array[j],array[i]
        temp=array[j]
  print("Sorted list using insertion sort: ",array)
      

def shellsort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2
    print("Sorted list using shellsort is: ",array[:5])

if __name__=="__main__":
    students_per=[]
    n=int(input("Enter number of students: "))
    for i in range(n):
        students_per.append(int(input("Enter Percentage: ")))
    insertion(students_per)
    shellsort(students_per,n)
