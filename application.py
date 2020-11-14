from flask import (Flask, render_template, request, redirect, url_for)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/bubble')
def bubble():
    return render_template("bubble.html")
@app.route('/bubble', methods=['GET', 'POST'])
def bubbleSort():
    bubbleList = request.form["bubbleList"]
    bubbleList = bubbleList.replace(",", " ")
    bubbleList = bubbleList.split()
    for i in range(len(bubbleList)):
        bubbleList[i] = int(bubbleList[i])
    for i in range(len(bubbleList)):
        for j in range(len(bubbleList)-i-1):
            if bubbleList[j] > bubbleList[j+1]:
                bubbleList[j], bubbleList[j+1] = bubbleList[j+1], bubbleList[j]
    for i in range(len(bubbleList)):
        bubbleList[i] = str(bubbleList[i])
    bubbleList = ", ".join(bubbleList)
    bubbleOutput = bubbleList
    return bubbleOutput



@app.route('/merge')
def merge():
    return render_template('merge.html')
@app.route('/merge', methods=['GET', 'POST'])
def mergeSortSetup():
    mergeList = request.form["mergeList"]
    mergeList = mergeList.replace(",", " ")
    mergeList = mergeList.split()
    mergeList = mergeSort(mergeList)
    return mergeList
def mergeSort(mergeList):
    if len(mergeList) == 1:
        return mergeList
    else:
        mid = int(len(mergeList) / 2)
        left = mergeList[:mid]
        right = mergeList[mid:]
        mergeSort(left)
        mergeSort(right)
        leftIndex = 0
        rightIndex = 0
        mergeIndex = 0
        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                mergeList[mergeIndex] = left[leftIndex]
                leftIndex += 1
            else:
                mergeList[mergeIndex] = right[rightIndex]
                rightIndex += 1
            mergeIndex += 1
        while leftIndex < len(left):
            mergeList[mergeIndex] = left[leftIndex]
            leftIndex += 1
            mergeIndex += 1
        while rightIndex < len(right):
            mergeList[mergeIndex] = right[rightIndex]
            rightIndex += 1
            mergeIndex += 1
        mergeList = ",".join(mergeList)
        return mergeList

@app.route('/linear')
def linear():
    return render_template('linear.html')
@app.route('/linear', methods=['GET', 'POST'])
def linearSearch():
    linearList = request.form["linearList"]
    linearValue = request.form["linearValue"]
    linearList = linearList.replace(",", " ")
    linearList = linearList.split()
    found = False
    i = 0
    while found == False and i < len(linearList):
        if linearList[i] == linearValue:
            found == True
            return "Your number is in position", i+1, "in the list"
        else:
            i += 1
    return "Number not in list"

@app.route('/binary')
def binary():
    return render_template("binary.html")
@app.route('/binary', methods=['GET', 'POST'])
def binarySearchSetup():
    binaryList = request.form["binaryList"]
    binaryValue = request.form["binaryValue"]
    originalArrayPosition = 0
    outputThis = binarySearch(binaryList, binaryValue, originalArrayPosition)
    return outputThis
def binarySearch(binaryList, binaryValue, oap):
    binaryValue = int(binaryValue)
    if "," in binaryList:
        binaryList = binaryList.replace(",", " ")
        binaryList = binaryList.split()
    for i in range(len(binaryList)):
        binaryList[i] = int(binaryList[i])
    if len(binaryList) == 1:
        if binaryValue == binaryList:
            return "Your number is the only one in the list"
        else:
            return "Number not found"
    mid = int(len(binaryList) / 2)
    left = binaryList[:mid]
    right = binaryList[mid:]
    if binaryValue < binaryList[mid]:
        binarySearch(left, binaryValue, oap)
    elif binaryValue > binaryList[mid]:
        oap += (len(binaryList)-mid)
        binarySearch(right, binaryValue, oap)
    else:
        return "Your number is at position", (mid+oap), "in the list"
