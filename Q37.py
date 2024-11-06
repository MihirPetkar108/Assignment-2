import math

def findMean(elements):
    mean = 0
    for i in elements:
        i = int(i)
        mean += i
    mean /= len(elements)
    print(mean)

def findMedian(elements):
    if(len(elements)%2 == 0):
        centre1 = (len(elements)//2) - 1
        centre2 = centre1 + 1

        num = (elements[centre1] + elements[centre2])/2
        return num
    else:
        center = len(elements)//2
        return elements[center]


elements = list(input("Enter elements(seperate using space): ").split(" "))
elements = [4,5,3,2,1,2]

findMean(elements)
print(findMedian(elements))