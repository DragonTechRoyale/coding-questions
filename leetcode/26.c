#include <stdio.h>
#include <strings.h>
#include "../include/array_funcs.h"

int allNumsSame(int* nums, int numsSize)
{
    int i=0;
    for (i=0; i<numsSize-1; i++)
    {
        if (nums[i] != nums[i+1])
        {
            return 0; // false
        }
    }

    return 1; // true
}

int removeDuplicates(int* nums, int numsSize){
    int i=0;
    int j=0;
    int tmp=0;

    if (allNumsSame(nums, numsSize) == 1)
    {
        return 1;
    }

    for (i=0; i<numsSize-1; i++)
    {
        tmp=i;

        while(tmp<=numsSize-1)
        {
            if (nums[tmp] > nums[i])
            {
                nums[i+1] = nums[tmp];
                j++;
                if (nums[tmp] == nums[numsSize-1])
                {
                    i = numsSize-1; // Stop the for loop, we got all the numbers.
                    j++;
                }
                break;
                
            }
            tmp++;
        }
    }
    
    return j;
}


int main()
{
    size_t size = 2;
    int nums[] = { 1,1 };
    int j = removeDuplicates(nums, size);
    printf("j: %d \n", j);
    printArr(nums, size);
}