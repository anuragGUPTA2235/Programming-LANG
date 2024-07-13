#include<stdio.h>

int prime_checker(int number)
{
    if(number < 2)
            return -1;
    else if(number == 2)
    {
        return 800;
    }
    else{
        for(int i = 2;i<=number/2;++i)
        {
           if(number%i==0)
                return 800;
        }
        return -1;
    }


}


int main()
{
    printf("prime number checker program\n");
    int number = 9;
    int res = prime_checker(number);
    printf("%d\n",res);
    return 0;
}
