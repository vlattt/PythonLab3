def bucketsort(m):
    bucketsort = []
    k = 0
    for i in range(len(m)):
        bucketsort.append([])
    for j in m:
        index = (10 // j)
        bucketsort[index].append(j)
    for i in range(len(m)):
        bucketsort[i] = sorted(bucketsort[i])
    for i in range(len(m)):
        for j in range(len(bucketsort[i])):
            m[k] = bucketsort[i][j]
            k += 1
    return m

m = [70, 12, 11, 78, 90, 33, 4, 51, 57, 10, 41, 22, 19, 88, 97, 13, 31, 40]
print(bucketsort(m))
