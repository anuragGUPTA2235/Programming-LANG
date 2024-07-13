def bricks_req(num):
    base = 2
    other_base = 5
    if num == 1:
        return 2
    else:
        for i in range(1,num):
            base = base + (other_base)
            other_base += 3

    return base
            
if __name__ =="__main__":
    num = int(input())
    bricks = bricks_req(num)
    print(bricks) 
