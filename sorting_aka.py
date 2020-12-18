from tkinter import*
from tkinter import ttk
import random
import time
import sys
import threading

root = Tk()
root.title('sorting')
root.maxsize(1920, 1080)
root.config(bg='black')

#variable
selected_alg = StringVar()
data = []
data2 = []


def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 1
    spacing = 1
    normalizeData = [i / max(data) for i in data]
    for i, height in enumerate(normalizeData):
        #top
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #botton
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()


def drawData2(data2, colorArray):
    canvas2.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data2) + 1)
    offset = 1
    spacing = 1
    normalizeData = [i / max(data2) for i in data2]
    for i, height in enumerate(normalizeData):
        #top
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #botton
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas2.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas2.create_text(x0+2, y0, anchor=SW, text=str(data2[i]))
    root.update_idletasks()


def buat():
    global data
    global data2

    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 100
    try:
        size = int(sizeEntry.get())
    except:
        size = 50

    if minVal < 0:
        minVal = 0
    if maxVal > 100:
        maxVal = 100
    if size > 1000 or size < 3:
        size = 50
    if minVal > maxVal:
        minVal, maxVal = maxVal, minVal

    data = []
    data2 = []

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    data2 = data.copy()

    drawData(data, ['white' for x in range(len(data))])
    drawData2(data2, ['white' for x in range(len(data2))])


def combSort(data, drawData):
    start_time2 = time.time()
    gap = len(data)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.30))  
        swaps = False
        for i in range(len(data) - gap):
            j = i+gap
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                swaps = True
                drawData(data, ['green' if x == i or x ==j else 'white' for x in range(len(data))])
                time.sleep(0.0)
    Label(text=(" %s seconds" % (time.time() - start_time2))).grid(row=1, column=0, padx=5, pady=5)


def insertion_sort(data2, drawData2):
    start_time2 = time.time()
    for i in range(1, len(data2)):
        key = data2[i]
        j = i-1
        while j >= 0 and key < data2[j]:
            data2[j+1] = data2[j]
            drawData2(data2, ['green' if x == j or x == key else 'white' for x in range(len(data))])
            time.sleep(0.0)
            j -= 1
        data2[j+1] = key
    Label(text=("%s seconds" % (time.time() - start_time2))).grid(row=1, column=2, padx=5, pady=5)

def startAlgorithm():
    global data
    global data2
    threading.Thread(target=insertion_sort, args=(data2, drawData2)).start()
    threading.Thread(target=combSort, args=(data, drawData)).start()


Label(text="").grid(row=1, column=0, padx=5, pady=5)
Label(text="").grid(row=1, column=2, padx=5, pady=5)


#frame

Label(text="Comb Sort").grid(row=0, column=0, padx=5, pady=5)
canvas = Canvas(root, width=600, height=380, bg='silver')
canvas.grid(row=4, column=0, padx=10, pady=5)

Label(text="Insertion Sort").grid(row=0, column=2, padx=5, pady=5)
canvas2 = Canvas(root, width=600, height=380, bg='silver')
canvas2.grid(row=4, column=2, padx=10, pady=5)
Button(text="Start", command=startAlgorithm, bg="silver").grid(row=1, column=1, padx=5, pady=5)


#UI
#row[1]
Button(text="random", command=buat, bg='yellow').grid(row=0, column=1, padx=5, pady=5)


root.mainloop()
