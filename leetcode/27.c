#include <stdio.h>
#include "../include/array_funcs.h"

int removeElement(int* nums, int numsSize, int val){
    int i = 0;
    int c = 0;
    int k = nonValNums(nums, numsSize, val);
    int tmp = 0;
    int prevTmp = 0;

    for (; i<numsSize-1; i++)
    {
        c = nums[i];
        tmp=i;
        while (nums[i] == val && prevTmp != i)
        {
            nums[i] = nums[tmp+1];
            c = nums[i];
            tmp++;
        }

        prevTmp = tmp;
    }

    return k;
}

int main()
{
    size_t numsSize = 8;
    int nums[] = {0,1,2,2,3,0,4,2};
    numsSize = removeElement(nums, numsSize, 2);
    printArr(nums, numsSize);
}