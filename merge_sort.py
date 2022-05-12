def divide(list):
  if len(list)>1:
    mid=len(list)//2
    left=list[:mid]
    right=list[mid:]
     
    divide(left)
    divide(right)

    merge(left,right,list)

def merge(a,b,list):
  i=j=k=0
  while i<len(a) and j<len(b):
    if a[i]<b[j]:
      list[k]=a[i]
      i=i+1
    else:
      list[k]=b[j]
      j=j+1
    k=k+1

  while i<len(a):
        list[k] = a[i]
        i+=1
        k+=1

  while j<len(b):
        list[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
  list=[]
  n=int(input("Enter no of elements "))
  for i in range(n):
    a=int(input("Enter elements "))
    list.append(a)

  divide(list)
  print(list)
