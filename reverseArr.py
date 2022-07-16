def reverseArray(a):
    # Write your code here
    reversedArr = []
    length = len(a) - 1
    currentIndex = 0
    while length >= 0:
        reversedArr.append(a[length])
        length = length - 1
        currentIndex = currentIndex + 1
    
    return reversedArr

arr = [1,2,3,4]

reversedArr = reverseArray(arr)
print(reversedArr)
