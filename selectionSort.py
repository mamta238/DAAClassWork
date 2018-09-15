
import sys


def minElement(a,n):
	l=len(a)
	min=a[n]
	pos=n
	for i in range(n+1,l):
		if min>a[i]:
			min=a[i]
			pos=i
	return pos			

def selectSort(a):
	l=len(a)
	for i in range(0,(l-1)):
		min=a[i]
		pos=minElement(a,i+1)	
		if a[pos]<min:		
			a[i]^=a[pos]
			a[pos]^=a[i]
			a[i]^=a[pos]
	print(a)			 

def main(a):
	arr=[]
	l=int(input("Enter length:"))
	print("Enter elements:")
	for i in range(0,l):
		arr.append(int(input()))
	selectSort(arr)
		
if __name__=='__main__':
	main(sys.argv)
