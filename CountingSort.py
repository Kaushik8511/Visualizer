import time

def countingSort(arr,visualize,sleep_time):
	max_element = int(max(arr)) 
	min_element = int(min(arr)) 
	color = ['cyan']*len(arr)
	range_of_elements = max_element - min_element + 1
	count_arr = [0 for _ in range(range_of_elements)] 
	output_arr = arr.copy() 
	color2 = ['cyan']*len(arr)
	for i in range(0, len(arr)):
		color[i] = 'red'
		visualize(arr,color)
		time.sleep(sleep_time)
		color[i] = 'cyan'
		count_arr[arr[i]-min_element] += 1
	for i in range(1, len(count_arr)): 
   		count_arr[i] += count_arr[i-1]
	for i in range(len(arr)-1, -1, -1):
		color2[i] = '#FF00FF'
		visualize(arr,color2)
		color2[i] = '#FFEFD5'
		time.sleep(3*sleep_time)
		output_arr[count_arr[arr[i] - min_element] - 1] = arr[i] 
		color[count_arr[arr[i] - min_element] - 1] = '#FF8C00'
		visualize(output_arr,color)
		color[count_arr[arr[i] - min_element] - 1] = 'green'
		time.sleep(sleep_time)
		count_arr[arr[i] - min_element] -= 1
	for i in range(0, len(arr)):
		arr[i] = output_arr[i]
	return arr
