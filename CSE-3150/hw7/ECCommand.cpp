//
//  ECCommand.cpp
//  
//

#include "ECCommand.h"

// ******************************************************
// Implement command history

ECCommandHistory :: ECCommandHistory() 
{
  // your code goes here
}

ECCommandHistory :: ~ECCommandHistory()
{
  for (ECCommand* c : m_undoStack) delete c;
  for (ECCommand* c : m_redoStack) delete c;
  m_undoStack.clear();
  m_redoStack.clear();
}

void ECCommandHistory::ExecuteCmd( ECCommand *pCmd )
{
    if (!pCmd) return;
    for (ECCommand* c : m_redoStack) delete c;
    m_redoStack.clear();

    pCmd->Execute();
    m_undoStack.push_back(pCmd);
}

bool ECCommandHistory::Undo()
{
    if (m_undoStack.empty()) return false;
    ECCommand* cmd = m_undoStack.back();
    m_undoStack.pop_back();
    cmd->UnExecute();
    m_redoStack.push_back(cmd);
    return true;
}

bool ECCommandHistory::Redo()
{
    if (m_redoStack.empty()) return false;
    ECCommand* cmd = m_redoStack.back();
    m_redoStack.pop_back();
    cmd->Execute();
    m_undoStack.push_back(cmd);
    return true;
}