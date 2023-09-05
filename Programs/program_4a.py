import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
            
my_list=[]
for i in range(10):
 my_list.append(random.randint(0,50))
print("\n Unsortted list")
print(my_list)
print("Sorting using Inserton Sort")
insertion_sort(my_list)
print(my_list)

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
          list[k] = left_half[i]
          i += 1
          k += 1
        while j < len(right_half):
          list[k]=right_half[j]
          j += 1
          k += 1
    return list

my_list1=[]
for i in range(10):
    my_list1.append(random.randint(0,50))
print("\n Unsortted list")
print(my_list1)
print("Sorting using Merge Sort")
merge_sort(my_list1)
print(my_list1)
