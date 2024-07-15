num = int(input())
list = [items for items in range(1,num+1)]
#print(list)
start = 0
real_list = [0 for items in range(1,num+1)]
for i in range(0,len(list)):
    real_list[i] = start^list[i]
    ans = start ^list[i]
    start = ans
sum = 0
for _ in real_list:
    sum += _
print(sum)    
