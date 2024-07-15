def factorial(ans):
    prod = 1
    for items in range(1,ans+1):
        prod = prod * items
    return prod    
if __name__ == "__main__":
    num = 4
    ans = factorial(num)
    print(ans)
