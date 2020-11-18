data = [7,5,8,6,0,-1,-5,9]

print(data)

def insertion(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                # print(arr)
    return arr

print(insertion(data))

