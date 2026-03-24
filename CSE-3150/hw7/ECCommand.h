//
//  ECCommand.h
//  
//
//

#ifndef ECCommand_h
#define ECCommand_h

#include <vector>

// ******************************************************
// Implement command design pattern

class ECCommand
{
public:
    virtual ~ECCommand() {}
    virtual void Execute() = 0;
    virtual void UnExecute() = 0;
};

// ******************************************************
// Implement command history

class ECCommandHistory
{
public:
    ECCommandHistory();
    virtual ~ECCommandHistory();
    bool Undo();
    bool Redo();
    void ExecuteCmd( ECCommand *pCmd );
    
private:
    // your code goes here
    std::vector<ECCommand*> m_undoStack;
    std::vector<ECCommand*> m_redoStack;
};


#endif /* ECCommand_h */
