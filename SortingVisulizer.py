from tkinter import *
from tkinter import ttk
from InsertionSort import insertionSort
from BubbleSort import bubbleSort
from QuickSort import quickSort
from MergeSort import mergeSort
from HeapSort import heapSort
from CountingSort import countingSort
from SelectionSort import selectionSort
from RadixSort import radixSort
import random

root = Tk()
root.title('Sorting Visualizer')
root.maxsize(1100, 1200)
root.config(bg='#4AA292')

#variables
selected_alg = ""
arr = []

#function
def visualize(arr, colorArray):
    plot_area.delete("all")
    c_height = 550
    c_width = 1080
    x_width = c_width / (len(arr) + 1)
    offset = 15
    spacing = 5
    normalizedarr = [ i / max(arr) for i in arr]
    for i, height in enumerate(normalizedarr):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 550
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        plot_area.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        #plot_area.create_text(x0+2, y0, anchor=SW, text=str(arr[i]))
    
    root.update_idletasks()


def Generate_arr():
    global arr
    arr=[]
    try:
        minVal = int(min_value.get())
    except:
        minVal = 1
    try:
        maxVal = int(max_value.get())
    except:
        maxVal = 1000
    try:
        size = int(size_of_arr.get())
    except:
        size = 100

    if minVal < 0 : minVal = 0
    if size>200 or size < 3: size = 25
    if minVal > maxVal : minVal, maxVal = maxVal, minVal

    for i in range(size):
        arr.append(random.randrange(minVal, maxVal+1))

    visualize(arr, ['cyan' for x in range(len(arr))]) 

def main_func():
    global arr
    if not arr: return

    if algMenu.get() == 'Quick Sort':
        quickSort(arr, 0, len(arr)-1, visualize, speedScale.get())
    
    elif algMenu.get() == 'Bubble Sort':
        bubbleSort(arr, visualize, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        mergeSort(arr, visualize, speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        insertionSort(arr, visualize, speedScale.get())    

    elif algMenu.get() == 'Heap Sort':
        heapSort(arr, visualize, speedScale.get())        

    elif algMenu.get() == 'Count Sort':
        countingSort(arr, visualize, speedScale.get())
    
    elif algMenu.get() == 'Selection Sort':
        selectionSort(arr, visualize, speedScale.get())

    elif algMenu.get() == 'Radix Sort':
        radixSort(arr, visualize, speedScale.get())

    visualize(arr, ['green' for x in range(len(arr))])


plot_area = Canvas(root, width=1200, height=580, bg='white')
plot_area.grid(row=0, column=0, padx=10, pady=5)
UI_frame = Frame(root, width= 1200, height=200, bg='#23F9D2')
UI_frame.grid(row=1, column=0, padx=10, pady=5)




Label(UI_frame, text="Select: ", bg='grey').grid(row=0, column=0, padx=5, pady=5)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Heap Sort', 'Insertion Sort', 'Bubble Sort', 'Merge Sort','Count Sort','Selection Sort','Quick Sort','Radix Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)


speedScale = Scale(UI_frame, from_=0.06, to=1.0, length=150, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=4, pady=3)
Button(UI_frame, text="Start", command=main_func, bg='#E6DD22').grid(row=0, column=4, padx=5, pady=5)


Label(UI_frame, text="Size ", bg='grey').grid(row=1, column=0, padx=5, pady=5)
size_of_arr = Entry(UI_frame)
size_of_arr.grid(row=1, column=1, padx=5, pady=5)

Label(UI_frame, text="Min Value ", bg='grey').grid(row=1, column=2, padx=5, pady=5)
min_value = Entry(UI_frame)
min_value.grid(row=1, column=3, padx=5, pady=5)

Label(UI_frame, text="Max Value ", bg='grey').grid(row=1, column=4, padx=5, pady=5)
max_value = Entry(UI_frame)
max_value.grid(row=1, column=5, padx=5, pady=5)

Button(UI_frame, text="Generate array", command=Generate_arr, bg='#E6DD22').grid(row=0, column=3, padx=5, pady=5)

root.mainloop()