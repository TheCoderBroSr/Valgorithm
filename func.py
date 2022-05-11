import random

def rand_arr(length, range):
    data = []
    start, end = range

    while len(data) != length:
        data.append(random.randint(start, end))

    return data

def my_sort(arr, type): #Sorting is ascending by default
    state = []

    if type == "bubble":
        for _ in range(len(arr)):
            state.append(arr.copy())

            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return state