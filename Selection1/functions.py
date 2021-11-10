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

def quicksort(array, init=0, end=None):
    end = (end if end is not None else len(array))
    if  init < end:
        h = partition(array, init, end)
        quicksort(array, init, h)
        quicksort(array, h+1, end)
    return array
