import time
colors = {0:"#4682B4",1: "#7FFFD4",2:"#A52A2A",3:"#5F9EA0",4:"#FF7F50",5:"#B8860B",6:"#00008B",7:"#FF1493",8:"#FF00FF",9:"#F0E68C"}

def countingSort(arr, exp1,visualize,time_sleep): 
    color = ['#FFEFD5']*len(arr)
    n = len(arr)  
    output = [0]*(n) 
    count = [0]*(10) 
    for i in range(0, n): 
        ind = (arr[i]//exp1) 
        color[i] = colors[ind%10]
        visualize(arr,color)
        time.sleep(time_sleep)
        count[(ind)%10] += 1
    for i in range(1,10): 
        count[i] += count[i-1] 
    i = n-1
    color1 = color.copy()
    while i>=0: 
        ind = (arr[i]//exp1)
        output[count[(ind)%10 ]-1] = arr[i] 
        count[(ind)%10 ] -= 1
        color1[count[(ind)%10]-1] = color[i]
        i -= 1
    i = 0
    
    for i in range(0,len(arr)):
        arr[i] = output[i] 
        color[i] = color1[i]
        visualize(arr,color)
        time.sleep(time_sleep)
def radixSort(arr,visualize,time_sleep): 
    mx = max(arr) 
    exp = 1
    while mx//exp > 0: 
        countingSort(arr,exp,visualize,time_sleep) 
        exp *= 10
