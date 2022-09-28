import time

def mergeSort(arr, visualize, sleep_time):
    merge_sort_alg(arr,0, len(arr)-1, visualize, sleep_time)


def merge_sort_alg(arr, left, right, visualize, sleep_time):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(arr, left, middle, visualize, sleep_time)
        merge_sort_alg(arr, middle+1, right, visualize, sleep_time)
        merge(arr, left, middle, right, visualize, sleep_time)

def merge(arr, left, middle, right, visualize, sleep_time):
    visualize(arr, getColorArray(len(arr), left, middle, right))
    time.sleep(sleep_time)

    leftPart = arr[left:middle+1]
    rightPart = arr[middle+1: right+1]

    leftIdx = rightIdx = 0

    for arrIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                arr[arrIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                arr[arrIdx] = rightPart[rightIdx]
                rightIdx += 1
        
        elif leftIdx < len(leftPart):
            arr[arrIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            arr[arrIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    visualize(arr, ["green" if x >= left and x <= right else "#FFEFD5" for x in range(len(arr))])
    time.sleep(sleep_time)

def getColorArray(lenght, left, middle, right):
    colorArray = []

    for i in range(lenght):
        if i >= left and i <= right:
            if i <= middle:
                colorArray.append("#FF4500")
            else:
                colorArray.append("#FFA500")
        else:
            colorArray.append("#FFEFD5")

    return colorArray