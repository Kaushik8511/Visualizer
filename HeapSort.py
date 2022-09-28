import time

def getColor(n,size,i):
    color = ['#FFEFD5']*n
    color[i]='red'
    for i in range(size,n):
        color[i]='green'
    return color

def heapify(arr,i,size,visualize,sleep_time):
    color = getColor(len(arr),size,i)
    visualize(arr,color)
    time.sleep(sleep_time)
    left = 2*i + 1
    right = left + 1
    m = i
    if (left<size):
        color[left] = 'red'
        visualize(arr,color)
        time.sleep(sleep_time)
    if(left < size and arr[left]>arr[m]):
        m = left
    if (right<size):
        color[right] = 'red'
        visualize(arr,color)
        time.sleep(sleep_time)
    if(right < size and arr[right] >arr[m]):
        m = right
    if (m!=i):
        arr[m],arr[i] = arr[i],arr[m]
        heapify(arr,m,size,visualize,sleep_time)




def BuildHeap(arr,visualize,sleep_time):
    for i in range(int(len(arr)/2),-1,-1):
        heapify(arr,i,len(arr),visualize,sleep_time)

def getColor_1(n,size):
    color=['#FFEFD5']*n
    for i in range(size,n):
        color[i]='green'
    return color

def heapSort(arr,visualize,sleep_time):
    size = len(arr)
    BuildHeap(arr,visualize,sleep_time)
    for i in range(size-1):
        arr[size-1],arr[0]=arr[0],arr[size-1]
        size -= 1
        visualize(arr,getColor_1(len(arr),size))
        heapify(arr,0,size,visualize,sleep_time)
