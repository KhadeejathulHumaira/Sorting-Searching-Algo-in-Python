#Bubble Sort
def Bubble_Sort_asc(arr):
    for i in range(len(arr)):# This is for pass
        for j in range(len(arr)-i-1): # This inner loop is for checking the adjacent elements
            if arr[j]>arr[j+1]:
               arr[j+1],arr[j]=arr[j],arr[j+1]

def Bubble_Sort_desc(arr):
    for i in range(len(arr)):# This is for pass
        for j in range(len(arr)-i-1): # This inner loop is for checking the adjacent elements
            if arr[j]<arr[j+1]:
               arr[j+1],arr[j]=arr[j],arr[j+1]
if __name__=="__main__":
    arr=[]
    n=int(input("Enter the number of elements:"))
    print("Enter the elements of array:")
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    print(f"Before sorting:\t{arr}")
    Bubble_Sort_asc(arr)
    print(f"After sorting(Ascending Order):\t{arr}")
    Bubble_Sort_desc(arr)
    print(f"After sorting(Descending Order):\t{arr}")