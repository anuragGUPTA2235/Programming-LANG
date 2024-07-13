def pairs(sum,arr):
    pairs = []
    for i in range(len(arr)):
        complement = sum  - arr[i]
        if complement in arr[i+1:]:
            pairs.append([arr[i],complement])
    return pairs        


if __name__ == "__main__":
    sum = int(input())
    arr = input()
    arr = list(map(int,arr.split()))
    res = pairs(sum,arr)
    print(res)
    # brute force
    list = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                list.append([arr[i],arr[j]])
    print(list)            
