def quickSort(list, low, high):
    if low < high:
        pi = part(list, low, high)
        quickSort(list, low, pi-1)
        quickSort(list, pi+1, high)

def part(list,low,high):
  x=low
  pivot=list[low]
  while low<high:
    while low<len(list) and list[low]<=pivot:
      low+=1
    while list[high]>pivot:
      high=high-1
    if low<high:
      list[low],list[high]=list[high],list[low]
  list[x],list[high]=list[high],list[x]
  return high

if __name__ == '__main__':
  list=[]
  n=int(input("Enter no of students "))
  for i in range(n):
    a=float(input("Enter students percentage "))
    list.append(a)
  print("Unsorted list ",list)
  quickSort(list, 0, n-1)
  print("List after sorting ",list)
