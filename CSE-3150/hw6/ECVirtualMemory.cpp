#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <queue>
#include "ECVirtualMemory.h"
using namespace std;


//*****************************************************************************
// Virtual memory: consists of memory pages and a main memory with limited capacity
// Page: represented by an integer; main memory can hold up to K pages
// Page replacement: when the main memory reaches its limit (i.e., having K pages) 
// and a new page (not currently in memory) is to be add, 
// then need to swap out one current page to make room for this new page
// This class: use OPT or LRU algorithm

// Your code here

ECVirtualMemory::ECVirtualMemory(int cap) {
    capacity = cap;
    pageFaultsLRU = 0;
}

void ECVirtualMemory::AccessPage(int page) {
    history.push_back(page);

    if (pos.find(page) != pos.end()) {
        lruList.erase(pos[page]);
        lruList.push_front(page);
        pos[page] = lruList.begin();
        return;
    }

    pageFaultsLRU++;

    if ((int)lruList.size() == capacity) {
        int oldPage = lruList.back();
        lruList.pop_back();
        pos.erase(oldPage);
    }

    lruList.push_front(page);
    pos[page] = lruList.begin();
}

int ECVirtualMemory::GetNumPageFaults() const {
    return pageFaultsLRU;
}

int ECVirtualMemory::GetNumPagesInMainMemory() const {
    return (int)lruList.size();
}

int ECVirtualMemory::RunOpt() {
    set<int> memory;
    int faults = 0;

    for (int i = 0; i < (int)history.size(); i++) {
        int page = history[i];

        if (memory.find(page) != memory.end())
            continue;

        if ((int)memory.size() < capacity) {
            memory.insert(page);
            faults++;
            continue;
        }

        int pageToRemove = -1;
        int farthestUse = -1;

        for (int p : memory) {
            int next = -1;
            for (int j = i + 1; j < (int)history.size(); j++) {
                if (history[j] == p) {
                    next = j;
                    break;
                }
            }

            if (next == -1) {
                pageToRemove = p;
                break;
            }

            if (next > farthestUse) {
                farthestUse = next;
                pageToRemove = p;
            }
        }

        memory.erase(pageToRemove);
        memory.insert(page);
        faults++;
    }

    return faults;
}

int ECVirtualMemory::RunFIFO() {
    set<int> memory;
    queue<int> order;
    int faults = 0;

    for (int page : history) {
        if (memory.find(page) != memory.end())
            continue;

        faults++;

        if ((int)memory.size() == capacity) {
            int old = order.front();
            order.pop();
            memory.erase(old);
        }

        memory.insert(page);
        order.push(page);
    }

    return faults;
}
