import sys




def main(a):
	l=int(input("Enter number:"))
	print("Enter Array Elements")	
	arr=[]
	for i in range(0,l):
		arr+=[int(input())]
	for i in range(0,l):
		flag=0
		for j in range(0,(l-i-1)):
			if(arr[j]>arr[j+1]):
				flag=1
				arr[j]^=arr[j+1]
				arr[j+1]^=arr[j]
				arr[j]^=arr[j+1]
		if flag==0:
			break
	
	print(arr)			
			




if __name__=='__main__':
	main(sys.argv)
