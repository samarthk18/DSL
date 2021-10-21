net_bal=0
while True:
 str=input("Enter operation and amount: ")
 transaction=str.split(" ")
 type=transaction[0]
 amt=int(transaction[1])
 if type=="D" or type=="d":
		net_bal+=amt
 elif type=="W" or type=="w":
		net_bal-=amt
 else:
      pass
 str=input("want to continue (Y for yes) : ")
 if not (str[0] =="Y" or str[0] =="y"): 
   break

print("Balance available in your account",net_bal)
