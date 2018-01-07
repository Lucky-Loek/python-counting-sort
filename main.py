from random import randint

def main():
    unsortedList = createRandomList()
    print('Unsorted list' + str(unsortedList))
    print('Sorted list' + str(countingSort(unsortedList)))

def countingSort(unsortedList):
    maxValue = max(unsortedList)
    listLength = len(unsortedList)

    countList = [0] * (maxValue + 1)

    # Calculate frequencies
    for integer in unsortedList:
        countList[integer] += 1

    print('freq list: ' + str(countList))

    # Modify frequency list with a prefix sum so we can calculate what the 
    # starting position of every number in our unsorted list is
    startingIndex = 0
    for i in range(maxValue + 1):
        current = countList[i]
        countList[i] = startingIndex
        startingIndex += current

    print('shif list: ' + str(countList))

    # Write output array
    output = [0] * (listLength)
    for i in unsortedList:
        output[countList[i]] = i
        countList[i] += 1

    return output

def createRandomList():
    unsortedList = []
    for x in range(16384):
        unsortedList.append(randint(0, 999))
    return unsortedList

if __name__ == '__main__':
    main()