//CPE593, Assignment 5, LinkedList
//
// Author: Yupeng Cao
// ID:     10454637
//
// Instruction: Please use C++14 to compile the file

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Build the Linkedlist Data Type
// Here refers to reference[1].
class LinkedList{
private:
    class Node{
    public:
        int data;
        Node* next;
    };
    Node* head;
public:
    //Initialize the linkedlist
    LinkedList(): head(nullptr) {}
    //Add new element from the end of linkedlist
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
    //Add new element from the front of linkedlist
    void addStart(int v){    //O(1)
        Node* temp = new Node;
        temp-> data = v;
        temp-> next = head;
        head = temp;
    }
    //Remove the first element from linkedlist
    void removeStart(){
        if(head == nullptr)
            return;
        Node* temp = head;
        head = head->next;
        delete temp;
    }
    //Remove the last element from linkedlist
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
    //Obtain the size of linkedlist
    int size() const{
        int count = 0;
        for(Node* p = head; p != nullptr; p = p->next)
            count++;
        return count;
    }
    //Get the element from the linkedlist
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

//Process the input file.
//Here refers to reference[2].
void split(std::vector<std::string>& v,std::string c, std::string line) {
    std::string::size_type pos1, pos2;
    pos2 = line.find(c);
    pos1 = 0;
    while (std::string::npos != pos2)
    {
        v.push_back(line.substr(pos1, pos2 - pos1));
        pos1 = pos2 + c.size();
        pos2 = line.find(c, pos1);
    }
    if (pos1 != line.length()) {
        v.push_back(line.substr(pos1));
    }
}

int main() {
    std::cout << "step 1" << std::endl;
    LinkedList a; //create an empty linkedlist O(1)

    //Load '.dat' file to input the data.
    const std::string resources_path_name = "./hw5.dat";
    std::ifstream fin(resources_path_name);
    std::string line;
    while (std::getline(fin, line)) {
        if (line == "" || line == "\n") {
            continue;
        }
        std::vector<std::string> v;
        split(v, " ", line);
        for (int i = 0; i < v.size(); i++) {
            int temp = atoi(v[i].c_str());
            a.addEnd(temp);
        }
    }
    fin.close();
    for (int i = 0; i < a.size(); i++)
        std::cout << a.get(i) << " ";
    std::cout << std::endl;


    std::cout << "step 2" << std::endl;
    LinkedList odd;  //create an empty linkedlist to store odd element.
    LinkedList even; //create an empty linkedlist to store even element.
    for (int i = 0; i < a.size(); i++) {
        //Judge whether the number is odd.
        if (a.get(i) % 2 != 0) {
            odd.addEnd(a.get(i));
        } else {
            even.addEnd(a.get(i));
        }
    }
    for (int i = 0; i < odd.size(); i++)
        std::cout << odd.get(i) << " ";
    std::cout << endl;
    for (int i = 0; i < even.size(); i++)
        std::cout << even.get(i) << " ";
    std::cout << endl;

    std::cout << "step 3 Intergating two LinkedList " << std::endl;
    LinkedList final; //create an empty linkedlist.

    //Maybe odd.linkedlist and even.linkedlist have different length.
    //Therefore, we will compare the size first.
    if (odd.size() < even.size()) {
        for (int i = 0; i < odd.size(); i++) {
            final.addEnd(even.get(i));
            final.addEnd(odd.get(i));
        }
        for (int j = even.size() - odd.size() + 1; j < even.size(); j++) {
            final.addEnd(even.get(j));
        }
    } else {
        for (int i = 0; i < even.size(); i++) {
            final.addEnd(even.get(i));
            final.addEnd(odd.get(i));
        }
        for (int j = odd.size() - even.size() + 1; j < odd.size(); j++) {
            final.addEnd(odd.get(j));
        }
    }

    //Output the final linkedlist.
    std::cout << "step 4 " << std::endl;
    for (int i = 0; i < final.size(); i++)
        std::cout << final.get(i) << " ";
    std::cout << endl;
}

//Reference:
//[1]https://www.tutorialspoint.com/cplusplus-program-to-implement-singly-linked-list
//[2]http://www.cplusplus.com/doc/tutorial/files/