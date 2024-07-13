def choc_dist(m,n):
    min = 1000
    for i in range(0,len(n)):
        if i + m in range(0,len(n)+1):
            first = n[i]
            last = n[i+m-1]
            diff = abs(first - last)
            if diff < min:
                min = diff
    return min            

if __name__ == "__main__":
    m = int(input())
    n = input()
    n = list(map(int,n.split()))
    n.sort()
    minimum = choc_dist(m,n)
    print(minimum)
