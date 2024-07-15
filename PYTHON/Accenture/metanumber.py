nums = int(input())
counter = 0
for num in range(1,nums):
    if num % 1 == 0  and num % 2 == 0  and num % 4 ==0 and num % 8 == 0 and num % 10 != 0:
        counter += 1
print(counter)                         
