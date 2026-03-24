#include "ECReverseLinkedList.h"
#include <stdio.h>
#include <stdlib.h>

/* Reverse the given linked list */
/* pHead: head node pointer to the linked list */
/* return the head of the reversed linked list */
/* note: don't allocate any new space using malloc; you should be able to reverse the linked list by just changing the pointers */
struct ECLinkedListNode* ECReverseLinkedList( struct ECLinkedListNode *pHead )
{
  /* Your code goes here */
  struct ECLinkedListNode* prev = NULL;
  struct ECLinkedListNode* current = pHead;
  struct ECLinkedListNode* next = NULL;

  while (current != NULL) {
      next = current->pNext;
      current->pNext = prev;
      prev = current;
      current = next;
  }
  return prev;

}