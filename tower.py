def tower(n,a,c,b):
	if n==1:
		print("Move disk ",n," from ",a," to pole",c)
	else:
		tower(n-1,a,b,c)
		print("Move disk ",n," from ",a," to pole",c)  
		tower(n-1,b,c,a)
n=int(input("Enter number of disks:"))
tower(n,'A','C','B')