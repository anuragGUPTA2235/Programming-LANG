
def square_digits(num):
    square = 0
    while num!= 0:
        digit = num % 10
        square = square + (digit*digit)
        num = num // 10
    return square    
    

if __name__ == "__main__":
    print("welcome")
    num = int(input())
    list = []
    while(True):
        num = square_digits(num)
        if num == 1:
            print("happy number")
            break
        elif num in list:
            print(num)
            print("cycle detected")
            break
        list.append(num)
        
