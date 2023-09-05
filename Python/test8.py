import random
def insort(num):
    for i in range(0,len(num)):
        key=num[i]
        j=i-1
        while j>=0 and key<num[j]:
            num[j+1]=num[j]
            j-=1
        num[j+1]=key

def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_hf=arr[:mid]
        right_hf=arr[mid:]
        merge(left_hf)
        merge(right_hf)
        i=j=k=0
        while i<len(left_hf) and j<len(right_hf):
            if left_hf[i]<right_hf[j]:
                arr[k]=left_hf[i]
                i+=1
            else:
                arr[k]=right_hf[j]
                j+=1
            k+=1
        while i<len(left_hf):
            arr[k]=left_hf[i]
            i+=1
            k+=1
        while j<len(right_hf):
            arr[k]=right_hf[j]
            j+=1
            k+=1
    return arr
n=int(input("Enter the value of n: "))
my_list=[]
for i in range(n):
    my_list.append(random.randint(0,99))
print("Unsorted list: ",my_list)
insort(my_list)
print("Sorted list using insertion sort: ",my_list)

n=int(input("Enter the value of n: "))
my_list=[]
for i in range(n):
    my_list.append(random.randint(0,99))
print("Unsorted list: ",my_list)
merge(my_list)
print("Sorted list using merge sort: ",my_list)
