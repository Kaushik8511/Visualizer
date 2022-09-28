import time

def getColor(arr,i,j):
	color = ['#FFEFD5']*len(arr)
	color[j] = 'red'
	color[i] = 'green'
	return color

def insertionSort(arr,visualize,sleep_time):
	for i in range(1,len(arr)):
		visualize(arr,getColor(arr,i,i))
		time.sleep(sleep_time)
		key = arr[i]
		j=i-1
		while j>=0 and key<arr[j]:
			visualize(arr,getColor(arr,i,j))
			time.sleep(sleep_time)
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key



