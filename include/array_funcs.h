#include <stdio.h>

// Helper functions for c array questions

void printArr(int * nums, int numsSize)
{
    int i=0;
    printf("[ ");
    for (i=0; i<numsSize; i++)
    {
        if (i+1==numsSize)
        {
            printf("%d ",nums[i]);
        }
        else 
        {
            printf("%d, ",nums[i]);
        }
    }
    puts("]");
}

// Count all numbers in nums which aren't val 
int nonValNums(int* nums, int numsSize, int val)
{
    int i=0;
    int k=0;
    int c=0;

    for (; i<numsSize; i++)
    {
        c = nums[i];
        if (c != val)
        {
            k++;
        }
    }

    return k;
}