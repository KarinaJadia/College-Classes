#include "ECListNode.h"
#include "ECList.h"

// Linked list 
ECList :: ECList() : pHead(nullptr), numNodes(0)
{
}
  
// insert node with value val after a node
// if node is NULL, insert to the front
void ECList :: Insert(int val, ECListNode *pPre)
{
    ECListNode *pNew = new ECListNode(val);

    if (pPre == nullptr) {
        // Insert at front
        pNew->SetNext(pHead);
        pHead = pNew;
    } else {
        // Insert after pPre
        pNew->SetNext(pPre->GetNext());
        pPre->SetNext(pNew);
    }

    numNodes++;
}

// delete a node
void ECList :: Delete(ECListNode *pNode)
{
    if (pNode == nullptr || pHead == nullptr)
        return;

    if (pNode == pHead) {
        pHead = pHead->GetNext();
        delete pNode;
        numNodes--;
        return;
    }

    ECListNode *pPrev = pHead;
    while (pPrev != nullptr && pPrev->GetNext() != pNode) {
        pPrev = pPrev->GetNext();
    }

    if (pPrev != nullptr && pPrev->GetNext() == pNode) {
        pPrev->SetNext(pNode->GetNext());
        delete pNode;
        numNodes--;
    }
}

// get a node with value; if multiple nodes with the same value, return the first from head
ECListNode * ECList::GetNode(int val)
{
    ECListNode *p = pHead;
    while (p != nullptr) {
        if (p->GetValue() == val)
        return p;
        p = p->GetNext();
    }
    return nullptr;
}

// get the number of nodes in the list
int ECList:: GetSize() const
{
    return numNodes;
}

