#include "ECRBT.h"
#include <iostream>

int main() {
  // Create a new rooted binary tree
  {
    ECRootedBinaryTree tree;

    // Create root node with ID 1
    ECTreeNode *root = new ECTreeNode(1);

    // Set root of the tree
    tree.SetRoot(root);

    // Create more nodes
    ECTreeNode *node2 = new ECTreeNode(2);
    ECTreeNode *node3 = new ECTreeNode(3);
    ECTreeNode *node4 = new ECTreeNode(4);
    ECTreeNode *node5 = new ECTreeNode(5);

    // Build the tree
    root->SetLeftChild(node2);
    root->SetRightChild(node3);
    node2->SetLeftChild(node4);
    node2->SetRightChild(node5);

    // Test GetNumLeavesUnder()
    std::cout << "Number of leaf nodes under root: "
              << root->GetNumLeavesUnder() << std::endl; // Should output 2
    std::cout << "Number of leaf nodes under node2: "
              << node2->GetNumLeavesUnder() << std::endl; // Should output 2
  }


  return 0;
}
