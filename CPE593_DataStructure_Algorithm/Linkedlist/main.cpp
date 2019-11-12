#include <iostream>
using namespace std;

class LinkedList{
private:
    class Node{
    public:
        int data;
        Node* next;
    };
    Node* head;

public:
    LinkedList(): head(nullptr) {}
    void addEnd(int v){
        if(head == nullptr){
            head = new Node();
            head-> data = v;
            head-> next = nullptr;
            return;
        }
        Node* p;
        for (p = head; p->next != nullptr; p = p->next);
        Node* temp = new Node();
        temp-> data = v;
        temp-> next = nullptr;
        p-> next = temp;
    }
    void addStart(int v){    //O(1)
        Node* temp = new Node;
        temp-> data = v;
        temp-> next = head;
        head = temp;
    }
    void removeStart(){
        if(head == nullptr)
            return;
        Node* temp = head;
        head = head->next;
        delete temp;
    }
    void removeEnd(){
        if(head == nullptr)
            return;
        Node* p;
        if(p->next == nullptr){
            delete p;
            head = nullptr;
            return;
        }
        Node* q = p;
        p = p-> next;
        for(; p->next != nullptr; q = p, p = p->next);
        delete p;
        q-> next = nullptr;
    }

    int size() const{
        int count = 0;
        for(Node* p = head; p != nullptr; p = p->next)
            count++;
        return count;
    }

    int get(int i) const{
        for(Node* p = head; p != nullptr; i--, p = p->next)
            if(i == 0)
                return p->data;
        throw "Out of bounds";
    }
    class Iterator{
    private:
        Node* current;
    public:
        Iterator(LinkedList& list) : current(list.head) {}
        bool operator !() const {return current != nullptr;}
        void operator ++() {current = current->next;}
        int& operator *() const{ return current->data;}
    };
};

int main(){
    LinkedList a; //create an empty linkedlist O(1)
    a.addEnd(4);
    a.addStart(3);
    const int n = 100;
    for(int i = 0; i < n; i++){
        a.addEnd(i);  //O(n^2)
    }

    //for(int i = 0; i < a.size(); i++)
        //cout << a.get(i) <<" ";

    for (LinkedList::Iterator i = a; !i; ++i)
        *i *= 3;

    for (LinkedList::Iterator i = a; !i; ++i)
        cout << *i << ' ';
    cout << '\n';
}
