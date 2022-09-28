import time

def getColor(n,i,j):
	color = ['#FFEFD5']*n
	color[j] = color[j+1] = 'red'
	for k in range(n-i,n):
		color[k] = 'green'
	return color


def bubbleSort(arr, visualize, sleep_time):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            visualize(arr, getColor(len(arr),i,j) )
            time.sleep(sleep_time)
    visualize(arr, ['green' for x in range(len(arr))])