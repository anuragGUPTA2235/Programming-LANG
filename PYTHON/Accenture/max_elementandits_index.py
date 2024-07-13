def max_returner(arr):
    max = arr[0]
    hashmap = {}
    for index,val in enumerate(arr):
        hashmap[val] = index

    for items in range(len(arr)):
        if arr[items] > max:
            max = arr[items]

    return max,hashmap[max]            






if __name__ == "__main__":
    amount = int(input())
    arr = input()
    arr = list(map(int,arr.split()))
    max,index = max_returner(arr)
    print(max,index)
