# Merge Sort

def merge_sort(arr):
    n = len(arr)
    if n <= 1: return arr

    # Break
    larr = arr[:n//2]
    rarr = arr[n//2:]

    larr = merge_sort(larr)
    rarr = merge_sort(rarr)

    (n, m) = (len(larr), len(rarr))
    (i, j) = (0, 0)
    new_arr = []
    while(i<n and j<m):
        if larr[i] < rarr[j]:
            new_arr.append(larr[i])
            i += 1
        else:
            new_arr.append(rarr[j])
            j += 1
    while(i<n):
        new_arr.append(larr[i])
        i += 1
    while(j<m):
        new_arr.append(rarr[j])
        j += 1
    
    return new_arr



arr = [3, 1, 5, 2, 8, 5, 4]

print(merge_sort(arr))

