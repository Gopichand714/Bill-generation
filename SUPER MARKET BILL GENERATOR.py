
date=input("Enter today date:")
costumer_name=input("Enter the Costumer name: ")
costumer_ph_no = input("Enter Costumer phone number: ")
costumer_address=input("Enter Costumer Address: ")
if len(costumer_ph_no)!=10:
	print('''
	**you entered wrong phone  number check the number once again**
	''')
print('''


        **PRICE LIST OF EACH ITEM**


Rice = 40/kg
sugar= 30/kg
salt= 20/kg
Dal=60/kg
oats =100/kg
oil = 150/kg
Masala = 200/kg

  ''')
print(""*5+"Typr 'yes' if you need the item and enter quantity or Type 'no' if you donot want the item"+""*5)
print('''
''')
E=[] 
F=[]
G=[]
H=[]
a=input("Rice : ")
if a=="yes":
	E.append("Rice  ")
	F.append(40 )
	x=float(input("Enter the quantity in kgs: ")) 
	G.append(x)
	H.append(x*40)
elif a=="no":
	pass
else :
	print("error")
b=input("sugar: ")
if b == "yes":
	E.append("Sugar ")
	F.append(30 )
	y=float(input("Enter the quantity in kgs: "))
	G.append(y)
	H.append(y*30)
elif b=="no":
	pass
else:
	print("error")
c = input("salt: ")
if c=="yes":
	E.append("Salt  ")
	F.append(20 )
	z=float(input("Enter the quantity in kgs: "))
	G.append(z)
	H.append(z*20)
elif c=="no":
	pass
else:
	print("error")
d= input("Dal: ")
if d=="yes":
	E.append("Dal   ")
	F.append(60 )
	X=float(input("Enter the quantity in kgs: "))
	G.append(X)
	H.append(X*60)
elif d=="no":
	pass
else:
	print("error")
e=input("oats: ")
if e=="yes":
	E.append("Oats  ")
	F.append(100)
	Y=float(input("Enter the quantity in kgs: "))
	G.append(Y)
	H.append(Y*100)
elif e=="no":
	pass
else:
	print("error")
f= input("Oil: ")
if f=="yes":
	E.append("Oil   ")
	F.append(150)
	Z=float(input("Enter the quantity in kgs: "))
	G.append(Z)
	H.append(Z*150)
elif f=="no":
	pass
else:
	print("error")
g=input("Masala: ")
if g=="yes":
	E.append("Masala")
	F.append(200)
	xy=float(input("Enter the quantity in kgs: "))
	G.append(xy)
	H.append(xy*200)
elif g=="no":
	pass
else:
	print("error")
B=[a, b, c,d,e,f,g]
C=[]
D=[]
for i in B:
	if i=="yes":
		C.append(i)
print(''' 
Your Bill Is Printing......
''')
print("-"*60)
print("  "*9+"*"*5+"Gopi Super market"+"*"*5+"  "*7)
print("Date: ",date)
print("Costumer Name : "+costumer_name)
print("Costumer Phone Number : "+costumer_ph_no)
print("Costumer Address: "+costumer_address)
print('_'*60)
A=["S.no","Item","Price/kg","Qty.","Price",]
for i in A :
	print(i,end='      ')
print(" ")
for j in range(len(C)):
	print(j+1,"       ",E[j],'    ',F[j],'         ',G[j],'    ',H[j])
print("_"*60)
final_price=sum(H)
print("                               TOTAL PRICE : ",str(final_price))
gst=int(final_price*(2/100))
print("                                       GST : ",str(gst))
print("                                FINAL PRICE: ",str(final_price+gst))
print('''                            
          ✓✓✓Thank You, Visit Again✓✓✓
          ''')
print("-"*60)