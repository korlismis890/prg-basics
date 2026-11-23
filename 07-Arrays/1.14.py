def procedure_bubbleSort(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n - 1):
        for j in range(n - i - 2):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr