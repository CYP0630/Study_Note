class Trie {
private:
    class Node{
        Node* next[26];
        bool isWord;
        Node(){

        }
    };
    Node root;
public:
    Trie() {};
    ~Trie() {}
    Trie(const Trie& orig) = delete;
    Trie& operator = (const Trie& orig) = delete;

    void add(const char word[]);

    void remove(const char word[]);

    bool contains(const char word[]);

    bool containsPrefix(const char word[]);


};