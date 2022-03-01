def DuplicateOcc(arr):
    dupArr = []
    for i in arr:
        if arr[i] in dupArr:
            return arr[i]
        else:
            dupArr.append(arr[i])
    return None
arr = [1,2,1,3,2,1,1]
print(DuplicateOcc(arr))
