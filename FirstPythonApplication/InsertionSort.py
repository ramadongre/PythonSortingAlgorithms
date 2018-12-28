def insertion_sort(arr):

    for i in range(1,len(arr)):
        key = arr[i]
    
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key

    for t in arr:
        print(t)

unsortedArray = [11,10,9,5,0,8,7,15,6,5,4,3,2,1]


insertion_sort(unsortedArray)
