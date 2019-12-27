#include <iostream>
#include <string>
#include <map>

using namespace std;

class BinaryTree{
private:
    class Node {
    public:
        int val;
        Node *left;
        Node *right;

        // Initialize the Node structure
        Node(int v) : val(v), left(nullptr), right(nullptr) {}

        void inorder() {
            if (left != nullptr)
                left->inorder();
            cout << val << ' ';
            if (right != nullptr)
                right->inorder();
        }

        void preorder() {
            cout << val << ' ';
            if (left != nullptr)
                left->preorder();
            if (right != nullptr)
                right->preorder();
        }

        void postorder() {
            if (left != nullptr)
                left->postorder();
            if (right != nullptr)
                right->postorder();
            cout << val << ' ';
        }
    };
    Node* root;

public:
    BinaryTree(): root{nullptr} {}
    void add(int v){
        if (root = nullptr){
            root = new Node(v);
            return;
        }
        Node* p = root;
        while (true){
            if (v < p->val){
                if (p->left == nullptr){
                    p->left = new Node(v);
                    return;
                }
                p = p->left;
            } else{
                if (p->right == nullptr){
                    p->right = new Node(v);
                    return;
                }
                p = p-> right;
            }
        }
    }

    void inorder() const {
        if (root != nullptr)
            root -> inorder();
    }

    void preorder() const{
        if (root != nullptr)
            root -> preorder();
    }

    void postorder() const{
        if (root != nullptr)
            root -> postorder();
    }
};


int main() {

    BinaryTree b;
    b.add(3);
    b.add(1);
    b.add(4);
    b.add(1);
    b.add(5);
    b.add(9);

    b.inorder();
    cout << "\n\n";
    return 0;
}
