from copy import deepcopy
import hashlib
import matplotlib.pyplot as plt
import csv

class BloomFilter:
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.bloom_filter = [0] * m

    def _hashes(self, element):
        hashes = []

        for i in range(self.k):
            value = f"{element}_{i}".encode()
            h = int(hashlib.md5(value).hexdigest(), 16)
            hashes.append(h % self.m)

        return hashes

    def insertElement(self, element):
        for h in self._hashes(element):
            self.bloom_filter[h] = 1

    def checkElement(self, element):
        for h in self._hashes(element):
            if self.bloom_filter[h] == 0:
                return False
        return True

def testFilterM(start,end):
    false_positives = []
    inputs = 50

    for size in range(start, end):
        filter = BloomFilter(size, 3)
        fp = 0
        for i in range(inputs):
            filter.insertElement(i)
        for i in range(inputs, inputs * 2):    
            if (filter.checkElement(i)):
                fp += 1
        false_positives.append(fp)
    plt.plot(range(start, end), false_positives)
    plt.xlabel("Bloom Filter Size")
    plt.ylabel("False Positives")
    plt.title("Bloom Filter False Positive Rate")
    plt.show()
    
def testFilterK(k):
    false_positives = []
    inputs = 1000

    for hashing in range(0, k):
        filter = BloomFilter(10000, hashing)
        fp = 0
        for i in range(inputs):
            filter.insertElement(i)
        for i in range(inputs, inputs * 2):    
            if (filter.checkElement(i)):
                fp += 1
        false_positives.append(fp)
    plt.plot(range(k), false_positives)
    plt.xlabel("Bloom Filter Size")
    plt.ylabel("False Positives")
    plt.title("Bloom Filter False Positive Rate")
    plt.show()

#testFilterM(1,1000);
testFilterK(50);