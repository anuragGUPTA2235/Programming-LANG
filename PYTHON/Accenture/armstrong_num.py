## armstrong number
if __name__ == "__main__":
    num = 153
    temp = num
    sum_cube = 0
    while num!=0:
        digit = num%10
        sum_cube += pow(digit,3)
        num = num//10    
    if sum_cube == temp:
        print("armstrong number")
    else:
        print("not an armstrong number")        
