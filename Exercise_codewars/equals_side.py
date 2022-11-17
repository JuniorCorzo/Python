def equals_Side(arr):
    sum_rigth = 0
    sum_left = 0
    index = len(arr) / 2
    stop = False

    while stop:
        for i in range(0, index):
            sum_rigth += arr[i]
        
        for i in range(index, len(arr)):
            sum_left += arr[i]
        
        if sum_rigth == sum_left:
            return index
        if sum_rigth > sum_left:
            index += 1
        if sum_rigth < sum_left:
            index -= 1    