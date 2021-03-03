print ("""please select the operator to do  any mathematical calculation of 2 numbers : \n
1.Addition (+) \n
2.Substraction  (-)\n
3.Multiplication  (x)\n
4.Division  (/)\n""")
option = int(input('Enter the  function you  want to do : '))

if(option >= 1and option <= 4):
	print('Enter two numbers      :')
	n1= float(input())
	n2= float(input())

	if option ==1:
		sum = (n1 + n2)
		print("Sum of "+str(n1)+" + "+str(n2)+" = "+str(sum))
	elif option== 2:
		sub=(n1 - n2)
		print("Difference between "+str(n1)+" and "+str(n2)+" = "+str(sub))
	elif option==3:
		mult=(n1*n2)
		print("multiplication of"+str(n1)+"and"+str(n2)+"="+str(mult))
	elif option==4:
			div=(n1/n2)
			print("divison of"+str(n1)+"and"+str(n2)+"="+str(div))
else :
		 	print("Wrong input....!!")
		 	