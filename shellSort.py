
import sys


def shellSort(a,t):
    n=int(t/2)
    while(n>0):
     for i in range(n,t):
        j=i
        p=j-n
        while(p>=0):
            if(a[j]<a[p]):
                a[j]^=a[p]
                a[p]^=a[j]
                a[j]^=a[p]
                j=p
                p=j-n
            else:
                break
     n=int(n/2)
    print(a) 


def main(a):
    list1=[]
    length=int(input("Enter list length:"))
    print("Enter list elements:")
    for l in range(0,length):
        list1+=[int(input())]
    print(list1)
    shellSort(list1,length)

if __name__=='__main__':

    main(sys.argv)
