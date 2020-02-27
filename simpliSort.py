""" Simple Implementation of Various Sorting Algorithms """

def bubble(aList):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(aList) - 1):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                swapped = True
    return aList

def main():
    print(bubble([3,5,7,9,72,4,5,34,17,34,34]))

if __name__ == "__main__":
    main()


def gnome(aList):

    i = 0
    while i < len(aList):
        # if i == 0 and aList[i] >= aList[i - 1]:
        if aList[i + 1] >= aList[i - 1]:
            i += 1
        else:
            aList[i], aList[i - 1] = aList[i - 1], aList[i]
            i -= 1

def main():
    print(bubble([3,5,7,9,72,4,5,87,17,66,34]))

if __name__ == "__main__":
    main()


def insertion(aList):

    for i in range(len(aList)):
        value = array[i] 

        while i > 0 and aList[i - 1] > value:
            aList[i] = aList[i - 1]
            i -= 1

        array[i] = value

def main():
    print(bubble([3,5,7,9,72,4,5,12,17,81,34]))

if __name__ == "__main__":
    main()


def merge(aList):

    if len(aList) > 1:
        mid = len(aList) // 2
        left_half = aList[ :mid]
        right_half = aList[mid: ]

        merge(left_half)
        merge(right_half)

        i = j = k = 0
        while i  < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                aList[k] = left_half[i]
                i += 1
            else:
                aList[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            aList[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            aList[k] = right_half[j]
            j += 1
            k += 1

    return aList

def main():
    print(merge([3,5,7,9,72,4,5,12,17,81,34]))

if __name__ == "__main__":
    main()


def merge(aList):

    if len(aList) > 1:
        mid = len(aList) // 2
        left_half = aList[ :mid]
        right_half = aList[mid: ]

        merge(left_half)
        merge(right_half)

        i = j = 0
        while i + j < len(aList):
            if j == len(right_half) or (i < len(left_half) and left_half[i] < right_half[j]):
                aList[i + j] = left_half[i]
                i += 1
            else:
                aList[i + j] = right_half[j]
                j += 1

    return aList

# print(merge([3,5,7,9,72,4,5,12,17,81,34]))


def partition(data, low, high):
    
    pivot = data[high]
    partition_index = low
    for i in range(low, high):
        if data[i] <= pivot:
            data[i], data[partition_index] = data[partition_index], data[i]
            partition_index += 1
    data[high], data[partition_index] = data[partition_index], data[high]
    # print(data)
    return partition_index


print(partition([2,3,6,7,5,19,1,4,77,65,11], 0, 10))


def quick(aList, low, high):
    if high <= low:
        return
    j = partition(aList, low, high)
    quick(aList, low, j - 1)
    quick(aList, j + 1, high)


print(quick([82,7,30,73,9,4], 0, 5))