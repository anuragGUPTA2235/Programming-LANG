def min_penalty(num,arr):
    arr.sort()
    ans = 0
    for i in range(len(arr)-1):
         ans = ans + (arr[i+1] - arr[i])
    return ans

  




if __name__ == "__main__":
    num  = int(input())
    arr = input()
    arr = list(map(int,arr.split()))
    ans = min_penalty(num,arr)
    print(ans)

