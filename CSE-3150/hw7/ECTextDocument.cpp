//
//  ECTextDocument.cpp
//  
//
//

#include "ECTextDocument.h"
#include <iostream>
#include <cctype>
#include <algorithm>

using namespace std;

// **********************************************************
// Commands
// command classes are defined here and use the ECTextDocument APIs

class InsertCommand : public ECCommand {
public:
    InsertCommand(ECTextDocument &d, int p, const std::vector<char> &data)
      : doc(d), pos(p), chars(data) {}
    void Execute() override {
        // insert chars in order
        for (size_t i = 0; i < chars.size(); ++i) {
            int insertPos = pos + (int)i;
            doc.InsertCharAt(insertPos, chars[i]);
        }
    }
    void UnExecute() override {
        // remove inserted chars
        for (size_t i = 0; i < chars.size(); ++i) {
            // always remove at original pos (characters shift left)
            doc.RemoveCharAt(pos);
        }
    }
private:
    ECTextDocument &doc;
    int pos;
    std::vector<char> chars;
};

class RemoveCommand : public ECCommand {
public:
    RemoveCommand(ECTextDocument &d, int p, int len)
      : doc(d), pos(p), lenToRemove(len) {}
    void Execute() override {
        removed.clear();
        for (int i = 0; i < lenToRemove && pos < doc.GetDocLen(); ++i) {
            removed.push_back(doc.GetCharAt(pos));
            doc.RemoveCharAt(pos);
        }
    }
    void UnExecute() override {
        // re-insert removed chars
        for (size_t i = 0; i < removed.size(); ++i) {
            doc.InsertCharAt(pos + (int)i, removed[i]);
        }
    }
private:
    ECTextDocument &doc;
    int pos;
    int lenToRemove;
    std::vector<char> removed;
};

class CapCommand : public ECCommand {
public:
    CapCommand(ECTextDocument &d, int p, int len) : doc(d), pos(p), lenToCap(len) {}
    void Execute() override {
        old.clear();
        for (int i = 0; i < lenToCap && pos + i < doc.GetDocLen(); ++i) {
            char oldc = doc.GetCharAt(pos + i);
            old.push_back(oldc);
            doc.SetCharAt(pos + i, (char)toupper((unsigned char)oldc));
        }
    }
    void UnExecute() override {
        for (size_t i = 0; i < old.size(); ++i) {
            doc.SetCharAt(pos + (int)i, old[i]);
        }
    }
private:
    ECTextDocument &doc;
    int pos;
    int lenToCap;
    std::vector<char> old;
};

class LowerCommand : public ECCommand {
public:
    LowerCommand(ECTextDocument &d, int p, int len) : doc(d), pos(p), lenToLower(len) {}
    void Execute() override {
        old.clear();
        for (int i = 0; i < lenToLower && pos + i < doc.GetDocLen(); ++i) {
            char oldc = doc.GetCharAt(pos + i);
            old.push_back(oldc);
            doc.SetCharAt(pos + i, (char)tolower((unsigned char)oldc));
        }
    }
    void UnExecute() override {
        for (size_t i = 0; i < old.size(); ++i) {
            doc.SetCharAt(pos + (int)i, old[i]);
        }
    }
private:
    ECTextDocument &doc;
    int pos;
    int lenToLower;
    std::vector<char> old;
};

class ReplaceCommand : public ECCommand {
public:
    ReplaceCommand(ECTextDocument &d, int p, int len, const std::vector<char> &ins)
      : doc(d), pos(p), lenToReplace(len), toInsert(ins) {}
    void Execute() override {
        removed.clear();
        // remove lenToReplace chars starting at pos (save them)
        for (int i = 0; i < lenToReplace && pos < doc.GetDocLen(); ++i) {
            removed.push_back(doc.GetCharAt(pos));
            doc.RemoveCharAt(pos);
        }
        // insert new chars
        for (size_t i = 0; i < toInsert.size(); ++i) {
            doc.InsertCharAt(pos + (int)i, toInsert[i]);
        }
    }
    void UnExecute() override {
        // remove the inserted chars
        for (size_t i = 0; i < toInsert.size(); ++i) {
            doc.RemoveCharAt(pos);
        }
        // re-insert removed chars
        for (size_t i = 0; i < removed.size(); ++i) {
            doc.InsertCharAt(pos + (int)i, removed[i]);
        }
    }
private:
    ECTextDocument &doc;
    int pos;
    int lenToReplace;
    std::vector<char> toInsert;
    std::vector<char> removed;
};

// **********************************************************
// Controller for text document

ECTextDocumentCtrl :: ECTextDocumentCtrl(ECTextDocument &docIn) 
: doc(docIn), history()
{
}

ECTextDocumentCtrl :: ~ECTextDocumentCtrl()
{
    // history destructor will clean allocated commands
}

void ECTextDocumentCtrl :: InsertTextAt(int pos, const std::vector<char> &listCharsToIns)
{
  // bounds: allow insertion at end
  int p = pos;
  if (p < 0) p = 0;
  if (p > doc.GetDocLen()) p = doc.GetDocLen();
  ECCommand *cmd = new InsertCommand(doc, p, listCharsToIns);
  history.ExecuteCmd(cmd);
}

void ECTextDocumentCtrl :: RemoveTextAt(int pos, int lenToRemove)
{
  int p = pos;
  if (p < 0) p = 0;
  if (p >= doc.GetDocLen() || lenToRemove <= 0) return;
  ECCommand *cmd = new RemoveCommand(doc, p, lenToRemove);
  history.ExecuteCmd(cmd);
}

void ECTextDocumentCtrl :: CapTextAt(int pos, int lenToCap)
{
  if (lenToCap <= 0) return;
  int p = pos;
  if (p < 0) p = 0;
  ECCommand *cmd = new CapCommand(doc, p, lenToCap);
  history.ExecuteCmd(cmd);
}

void ECTextDocumentCtrl :: LowerTextAt(int pos, int lenToLower)
{
  if (lenToLower <= 0) return;
  int p = pos;
  if (p < 0) p = 0;
  ECCommand *cmd = new LowerCommand(doc, p, lenToLower);
  history.ExecuteCmd(cmd);
}

bool ECTextDocumentCtrl :: Undo()
{
  return history.Undo();
}

bool ECTextDocumentCtrl :: Redo()
{
  return history.Redo();
}

int ECTextDocumentCtrl :: Search(const std::vector<char> &pattern) const
{
  // simple naive search
  if (pattern.empty()) return 0;
  int n = doc.GetDocLen();
  int m = (int)pattern.size();
  for (int i = 0; i + m <= n; ++i) {
    bool ok = true;
    for (int j = 0; j < m; ++j) {
      if (doc.GetCharAt(i + j) != pattern[j]) { ok = false; break; }
    }
    if (ok) return i;
  }
  return -1;
}

void ECTextDocumentCtrl :: ReplaceAt(int pos, int lenToReplace, const std::vector<char> &listCharsToIns)
{
  int p = pos;
  if (p < 0) p = 0;
  ECCommand *cmd = new ReplaceCommand(doc, p, lenToReplace, listCharsToIns);
  history.ExecuteCmd(cmd);
}

// **********************************************************
// Document for text document


ECTextDocument :: ECTextDocument() 
: listChars(), docCtrl(nullptr)
{
    docCtrl = new ECTextDocumentCtrl(*this);
}

ECTextDocument :: ~ECTextDocument()
{
    delete docCtrl;
    docCtrl = nullptr;
}

ECTextDocumentCtrl & ECTextDocument :: GetCtrl()
{
    return *docCtrl;
}

char ECTextDocument :: GetCharAt(int pos) const
{
    if (pos < 0 || pos >= (int)listChars.size()) return '\0';
    return listChars[pos];
}

void ECTextDocument :: InsertCharAt(int pos, char ch)
{
  int p = pos;
  if (p < 0) p = 0;
  if (p > (int)listChars.size()) p = (int)listChars.size();
  listChars.insert(listChars.begin() + p, ch);
}

void ECTextDocument :: RemoveCharAt(int pos)
{
  if (pos < 0 || pos >= (int)listChars.size()) return;
  listChars.erase(listChars.begin() + pos);
}

void ECTextDocument :: CapCharAt(int pos)
{
  if (pos < 0 || pos >= (int)listChars.size()) return;
  listChars[pos] = (char)toupper((unsigned char)listChars[pos]);
}

void ECTextDocument :: LowerCharAt(int pos)
{
  if (pos < 0 || pos >= (int)listChars.size()) return;
  listChars[pos] = (char)tolower((unsigned char)listChars[pos]);
}

void ECTextDocument :: SetCharAt(int pos, char ch)
{
  if (pos < 0 || pos >= (int)listChars.size()) return;
  listChars[pos] = ch;
}