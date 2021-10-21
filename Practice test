input("Enter Employee name ")
print("1.Manager")
print("2.Team leader")
print("3.Team member")
y=int(input("Choose your Designation:"))
if y==1:
  sal=2000
elif y==2:
  sal=1800
elif y==3:
  sal=1500
else:
  print("Enter correct month")
print("Enter '1' for Jan,March,May,July,Aug,Oct,Dec")
print("Enter '2' for Apr,June,Sept,Nov")
print("Enter '3' for Feb")
x=int(input("Enter appropriate number for appropriate month:"))
z=int(input("Enter number of present days: "))
ot=int(input("Enter number of over time days: "))
if z<=31:
  if x==1:
    print("Your total salary for the selected month is ",sal*31)
    print("Your salary for present days is ",sal*z)
    print("Your salary for overtime is ",(sal*ot)/2)
    print("Your total salary is ",sal*z+(sal*ot)/2)
  elif x==2:
    print("Your total salary for the selected month is ",sal*30)
    print("Your salary for present days is ",sal*z)
    print("Your salary for overtime is ",(sal*ot)/2)
    print("Your total salary is ",sal*z+(sal*ot)/2)
  elif x==3:
    print("Your total salary for the selected month is ",sal*28)
    print("Your salary for present days is ",sal*z)
    print("Your salary for overtime is ",(sal*ot)/2)
    print("Your total salary is ",sal*z+(sal*ot)/2)
  else:
    print("Enter correct month")
else:
  print("Please enter correct number of month")
