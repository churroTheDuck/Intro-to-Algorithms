from copy import deepcopy

bloom_filter = deepcopy([0] * 1000)

def insertElement(element):
    for i in range(3):
        bloom_filter[(hash(element) ^ hash(i))  % 1000] = 1
    
def containsElement(element):
    for i in range(3):
        if bloom_filter[(hash(element) ^ hash(i))  % 1000]:
            pass
        else:
            return False
    return True

insertElement(64)
print(containsElement(64))
print(containsElement(67))