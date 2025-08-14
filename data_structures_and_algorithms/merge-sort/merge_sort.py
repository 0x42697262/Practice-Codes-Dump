def conquer(L: list, R: list) -> list:
    sorted = []
    i = j = 0


    while ( i < len(L) and j < len(R) ):
        if L[i] <= R[j]:
            sorted.append(L[i])
            i += 1
        else:
            sorted.append(R[j])
            j += 1

    sorted.extend(L[i:])
    sorted.extend(R[j:])

    return sorted

def divide(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    L = divide(arr[:mid])
    R = divide(arr[mid:])

    return conquer(L, R)

lst = divide([2,4,1,6,8,5,3,7])
print(lst)
