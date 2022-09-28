import time

def partition(arr, start, end, visualize, sleep_time):
    correct_index = start
    pivot = arr[end]

    visualize(arr, getColor(len(arr), start, end, correct_index, correct_index))
    time.sleep(sleep_time)

    for j in range(start, end):
        if arr[j] < pivot:
            visualize(arr, getColor(len(arr), start, end, correct_index, j, True))
            time.sleep(sleep_time)

            arr[correct_index], arr[j] = arr[j], arr[correct_index]
            correct_index += 1

        visualize(arr, getColor(len(arr), start, end, correct_index, j))
        time.sleep(sleep_time)


    #swap pivot with correct_index value
    visualize(arr, getColor(len(arr), start, end, correct_index, end, True))
    time.sleep(sleep_time)

    arr[correct_index], arr[end] = arr[end], arr[correct_index]
    
    return correct_index

def quickSort(arr, start, end, visualize, sleep_time):
    if start < end:
        mid = partition(arr, start, end, visualize, sleep_time)

        #LEFT PARTITION
        quickSort(arr, start, mid-1, visualize, sleep_time)

        #RIGHT PARTITION
        quickSort(arr, mid+1, end, visualize, sleep_time)


def getColor(arrLen, start, end, correct_index, currIdx, isSwaping = False):
    colorArray = []
    for i in range(arrLen):
        #base coloring
        if i >= start and i <= end:
            colorArray.append('#FFEFD5')
        else:
            colorArray.append('white')

        if i == end:
            colorArray[i] = 'blue'
        elif i == correct_index:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == correct_index or i == currIdx:
                colorArray[i] = 'green'
    return colorArray