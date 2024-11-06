def sortInEvenOdd (arr) :
    arrEven = []
    arrOdd = []
    i = 0
    while (i < len(arr)):
        if arr[i] % 2 == 0:
            arrEven.append(arr[i])
        else:
            arrOdd.append(arr[i])
    
        i += 1
    
    arrEven.sort()
    arrOdd.sort()
    
    return arrEven + arrOdd

arr = [3,2,5,10,6,4,9]

print(sortInEvenOdd(arr))