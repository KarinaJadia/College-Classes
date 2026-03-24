#ifndef _EC_LIST_NODE_H
#define _EC_LIST_NODE_H

#include <iostream>

// Class for linked list node
class ECListNode
{
public:
  ECListNode() : value(0), pNext(nullptr) {}
  ECListNode(int v) : value(v), pNext(nullptr) {}

  ECListNode *GetNext() const { return pNext; }
  void SetNext(ECListNode *pn) { pNext = pn; }

  int GetValue() const { return value; }
  void SetValue(int v) { value = v; }

private:
  int value;
  ECListNode *pNext;
};

#endif
