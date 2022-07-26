#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    int val;
    struct ListNode *next;
} ListNode;


int listLength(struct ListNode* list){
    int len = 0;
    struct ListNode * current = list;

    while (current != NULL)
    {
        len++;
        current = current->next;
    }

    return len;
}

char * listToString(struct ListNode* list)
{
    int i = 0;
    int j = 0;
    int listLen = listLength(list);
    int printedOutputLen = (listLen*3)+3;
    char * printedOutput = (char *)malloc(printedOutputLen);
    struct ListNode * current = list;

    memset(printedOutput, NULL, printedOutputLen);
    printedOutput[0] = '[';

    for(i=0; i<listLen;i++)
    {
        j = (i*3)+1;
        printedOutput[j] = (char)((current->val) + (int)'0');
        if (i != listLen-1)
        {
            printedOutput[j+1] = ',';
            printedOutput[j+2] = ' ';
        }
        else
        {
            printedOutput[j+1] = ']';
        }
        current = current->next;
    }

    return printedOutput;
}

struct ListNode * addTwoLists(struct ListNode* list1, struct ListNode* list2)
{
    // Simply adds list2 to the end of list1
    struct ListNode * current1 = list1;

    while (current1->next != NULL)
    {
        current1=current1->next;
    }

    current1->next = list2;
    return list1;
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2)
{
    struct ListNode * current1;
    struct ListNode * current2;

    struct ListNode * merged;
    struct ListNode * mergedPos = merged;

    current1 = list1;
    current2 = list2;

    struct ListNode * newItem = (struct ListNode *)malloc(sizeof(struct ListNode));
    if (current1 == NULL)
    {
        return current2;
    }
    else if (current2 == NULL)
    {
        return current1;
    }

    if (current1->val <= current2->val)
    {
        newItem->val = current1->val;
        merged = newItem;
        mergedPos = merged;
        current1 = current1->next;
    }
    else
    {
        newItem->val = current2->val;
        merged = newItem;
        mergedPos = merged;
        current1 = current2->next;
    }
    
    while (0==0)
    {
        if (current1 == NULL)
        {
            merged = addTwoLists(merged, current2);
            break;
        }
        else if (current2 == NULL)
        {
            merged = addTwoLists(merged, current1);
            break;
        }
        else
        {
            newItem = (struct ListNode *)malloc(sizeof(struct ListNode));
            if (current1->val <= current2->val)
            {
                newItem->val = current1->val;
                current1 = current1->next;
            }
            else
            {
                newItem->val = current2->val;
                current2 = current2->next;  
            }
            mergedPos->next = newItem;
            mergedPos = mergedPos->next;
        } 
    }

    return merged;
}

int main()
{
    struct ListNode * list1_first = (struct ListNode *)malloc(sizeof(struct ListNode *));
    struct ListNode * list1_second = (struct ListNode *)malloc(sizeof(struct ListNode *));
    struct ListNode * list1_third = (struct ListNode *)malloc(sizeof(struct ListNode *));

    struct ListNode * list2_first = (struct ListNode *)malloc(sizeof(struct ListNode *));
    struct ListNode * list2_second = (struct ListNode *)malloc(sizeof(struct ListNode *));
    struct ListNode * list2_third = (struct ListNode *)malloc(sizeof(struct ListNode *));

    struct ListNode * merged;

    list1_first->val = 1;
    list1_first->next = list1_second;
    list1_second->val = 2;
    list1_second->next = list1_third;
    list1_third->val = 4;
    list1_third->next = NULL;

    list2_first->val = 1;
    list2_first->next = list2_second;
    list2_second->val = 3;
    list2_second->next = list2_third;
    list2_third->val = 4;
    list2_third->next = NULL;

    merged  = mergeTwoLists(list1_first, list2_first);

    printf("List 1 length: %d \n", listLength(list1_first));
    printf("List 2 length: %d \n", listLength(list2_first));

    printf("List 1: %s \n", listToString(list1_first));
    printf("List 2: %s \n", listToString(list2_first));

    printf("merged: %s \n", listToString(merged));
}
