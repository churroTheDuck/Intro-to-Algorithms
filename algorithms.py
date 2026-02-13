import time
import random
import math
from termcolor import cprint

def insertionSort(unsortedList):
    sortedList = unsortedList
    x = 0
    for i in range(1, len(sortedList)): # iterates through each element of the list
        x = i # x is a counter that goes from the current element to the bottom of the list
        while(x != 0 and sortedList[x] < sortedList[x - 1]): # loops until either counter reaches bottom of the list or a greater element is found
            sortedList[x], sortedList[x - 1] = sortedList[x - 1], sortedList[x] # swap element wiht element before it
            x -= 1
    return sortedList

def countingSort(unsortedList):
    sortedList = []
    min_val = min(unsortedList)
    max_val = max(unsortedList)
    bucketList = [0] * (max_val - min_val + 1) # creates buckets for each number between min and max of the list
    for i in range(0, len(unsortedList)): # iterates through each element of the list
        bucketList[unsortedList[i] - min_val] += 1 # checks the value of the element, then adds one to the element of the bucketList that has the index with the value
    for x in range(0, len(bucketList)):
        for y in range(0, bucketList[x]):
            sortedList.append(x)
    return sortedList

def radixSort(unsortedList):
    sortedList = unsortedList
    bucketList = [[] for _ in range(10)]
    digits = math.floor(math.log10(max(sortedList))) + 1 # finds the maximum number of digits in the list
    for digit in range(0, digits): # iterates through each digit
        bucketList = [[] for _ in range(10)]
        for i in range(0, len(sortedList)): # iterates through each element of the list
            bucketList[sortedList[i] // 10**digit % 10].append(sortedList[i]) # checks the current digit of the element, then adds the element to the corresponding location in the bucketList
        sortedList = []
        for bucket in bucketList: # adds bucketList items to the sorted list
            sortedList.extend(bucket)
    return sortedList

# Testing functions
def test(algorithm, size):
    cprint(algorithm, "blue", attrs=["bold"])
    unsortedList = list(range(size))
    random.shuffle(unsortedList)
    # cprint("Unsorted:", "red")
    # print(unsortedList)
    start = time.time()
    cprint("Sorted:", "green")
    print(algorithm(unsortedList))
    end = time.time()
    cprint(f"End - Start = {end - start} seconds", "white", "on_yellow")

# Testing
test(insertionSort, 100)
test(countingSort, 100)
test(radixSort, 100)