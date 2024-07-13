if __name__ == "__main__":
    round = int(input())
    list = [0 for items in range(0,round)]
    for level in range(len(list)):
        if level == 0:
            list = [1 for items in range(len(list))]
        elif level == len(list)-1:
            if list[-1] == 0:
             list[-1] = 1
            else:
               list[-1] = 0 
        else:
           new_lev = level + 1  # 2
           for i in range(len(list)):
              if (i + 1) % new_lev==0:  
                 if list[i] == 0:
                    list[i] = 1
                 else:
                    list[i] = 0  

        print(list)       
              
        

         
