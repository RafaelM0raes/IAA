def partition(array, init, end):
    pivo = array[end-1]
    for i in range(init, end):
        if array[i] > pivo:
            end += 1
        else:
            end += 1
            init += 1
            array[i], array[init-1] = array[init-1], array[i]
    return init-1

def selection2(array, i):
    end = len(array)
    q = partition(array, 0, len(array))
    if (end == 1):
        return array[0]
    if (i < q):
        return selection2(array[0:q-1], i)
    elif (i > q):
        return selection2(array[q:end], i-q)
    else:
        return array[q-1]
