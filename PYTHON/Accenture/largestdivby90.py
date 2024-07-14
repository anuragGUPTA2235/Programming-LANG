def largest_div_90(arr):
    list = []
    for items in arr:
        if items == 5:
            list.append(items)
       
    num = "" 
    flag = 0
    for items in list:
        num = num + str(items)
        number = int(num)
        if number % 9 == 0:
            flag  = 1
            break
    for items in arr:
        if items == 0:
            num = num + str(items)    
    return int(num) if flag == 1 else 0   

  
            

if __name__ == "__main__":
    arr = input()
    arr = list(map(int,arr.split())) 
    out = largest_div_90(arr)
    print(out)  
