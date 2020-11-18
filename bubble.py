data = [7,5,8,6,0,-1,-5]

print(data)

def bubble(arr):
    for i in range(len(arr), 1, -1):
        swap = True
        for j in range( 0, len(arr)-1):
            if( arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap = False
                print(arr)
        if(swap!=False):
            break
    return arr

print(bubble(data))