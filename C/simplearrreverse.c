#include<stdio.h>

int main()
{
    printf("welcome to c language\n");
    int arr[] = {1,2,4,6,7};
    int len = sizeof(arr)/sizeof(arr[0]);
    for(int i = 0;i<len;++i)
    {
         printf("%d\n",arr[i]);
    }

    int left = 0;
    int right = len - 1;
    while(left!=right)
    {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        ++left;
        --right;
    }
        for(int i = 0;i<len;++i)
    {
         printf("%d\n",arr[i]);
    }




    return 0;
}
