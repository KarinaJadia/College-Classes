//
//  ECTextDocumentTest.cpp
//  
//
//

#include <iostream>
#include "ECTextDocument.h"

using namespace  std;

static void Test1()
{
    //
    ECTextDocument doc;
    ECTextDocumentCtrl &docCtrl = doc.GetCtrl();
    vector<char> listText1;
    listText1.push_back('a');
    listText1.push_back('b');
    listText1.push_back('c');
    listText1.push_back('d');
    listText1.push_back('e');
    docCtrl.InsertTextAt(0, listText1);
    vector<char> listText2;
    listText2.push_back('f');
    listText2.push_back('g');
    listText2.push_back('h');
    int posIns = 2;
    docCtrl.InsertTextAt(posIns, listText2);
    //int lenDel = 2;
    //docCtrl.RemoveTextAt( posIns, lenDel );
    int posCap = 2;
    int lenCap = 5;
    docCtrl.CapTextAt( posCap, lenCap );
    int posLow = 3;
    int lenLow = 2;
    docCtrl.LowerTextAt( posLow, lenLow );
    
    cout << "Text: ";
    for(int i=0; i<doc.GetDocLen(); ++i)
    {
        cout << doc.GetCharAt(i);
    }
    cout << endl;
    
    // try undo/redo
    docCtrl.Undo();
    cout << "After undo, text: ";
    for(int i=0; i<doc.GetDocLen(); ++i)
    {
        cout << doc.GetCharAt(i);
    }
    cout << endl;
    
    docCtrl.Redo();
    cout << "After redo, text: ";
    for(int i=0; i<doc.GetDocLen(); ++i)
    {
        cout << doc.GetCharAt(i);
    }
    cout << endl;
}

static void TestSearchReplace()
{
    ECTextDocument doc;
    ECTextDocumentCtrl &docCtrl = doc.GetCtrl();
    // build text: abc test abc test xyz
    vector<char> text;
    const char *s = "abc test abc test xyz";
    for(const char *p=s; *p; ++p) text.push_back(*p);
    docCtrl.InsertTextAt(0, text);

    // search lowercase "test"
    vector<char> pat = {'t','e','s','t'};
    int pos = docCtrl.Search(pat);
    cout << "Search('test') pos: " << pos << endl;

    // replace it with uppercase
    vector<char> repl = {'T','E','S','T'};
    if(pos >= 0)
    {
        docCtrl.ReplaceAt(pos, (int)pat.size(), repl);
    }

    cout << "After ReplaceAt, text: ";
    for(int i=0; i<doc.GetDocLen(); ++i)
    {
        cout << doc.GetCharAt(i);
    }
    cout << endl;

    // undo and redo once to exercise history
    docCtrl.Undo();
    cout << "After undo, text: ";
    for(int i=0; i<doc.GetDocLen(); ++i)
    {
        cout << doc.GetCharAt(i);
    }
    cout << endl;

    docCtrl.Redo();
    cout << "After redo, text: ";
    for(int i=0; i<doc.GetDocLen(); ++i)
    {
        cout << doc.GetCharAt(i);
    }
    cout << endl;
}

int main()
{
    // test code
    Test1();
    TestSearchReplace();
    
    return 0;
}
