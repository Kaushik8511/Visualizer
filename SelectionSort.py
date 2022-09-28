import time

def selectionSort(arr,visualize,sleep_time):
	color = ['#FFEFD5']*len(arr)
	for i in range(len(arr)-1):
		color[i] = '#FF00FF'
		mn = i
		visualize(arr,color)
		time.sleep(sleep_time)
		for j in range(i+1,len(arr)):
			color[j] = 'red'
			visualize(arr,color)
			time.sleep(sleep_time)
			if (arr[mn]>arr[j]):
				if(mn!=i):color[mn] = '#FFEFD5'
				mn = j
				color[mn] = 'cyan'
			visualize(arr,color)
			time.sleep(sleep_time)
			if(j!=mn):color[j] = '#FFEFD5'

		arr[i],arr[mn] = arr[mn],arr[i]
		color[mn] = '#FFEFD5'
		color[i] = 'green'
