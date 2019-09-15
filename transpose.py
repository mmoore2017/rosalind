def transpositions(arr):
    trans = 0
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                trans += 1

    print(trans)


transpositions([5,7,1,3,5,2])


