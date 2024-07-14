def finalplace(stones,instruction):
    pos = 1
    j = 0
    for i in range(len(instruction)):
        if stones[j] == instruction[i]:
            print(stones[i],instruction[i])
            pos += 1
            j += 1
    return pos        

       
if __name__ == "__main__":
    stones = input()
    instruction = input()
    pos = finalplace(stones,instruction)
    print(pos)
