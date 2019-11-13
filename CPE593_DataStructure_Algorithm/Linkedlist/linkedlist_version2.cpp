#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
struct Node
{
	int data;
	Node* next;
	Node() { data = 0; next = NULL; }
};
Node* insert(int data, Node* p) {
	Node* newNode = new Node();
	newNode->data = data;
	newNode->next = NULL;
	p->next = newNode;
	p = newNode;
	return p;
}
Node* insert(Node* t, Node* p) {
	p->next = t;
	p = t;
	return p;
}

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
void printlist(Node* root) {
	Node* p = root->next;
	cout << "LIST\t";
	while (p != NULL) {
		cout << p->data << "\t";
		p = p->next;
	}
	cout << endl;
}

int main() {
	std::cout << "step 1" << std::endl;
	Node* rootA = new Node();
	Node* rootB = new Node();
	Node* p = rootA;
	Node* q = rootB;
	
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
			p = insert(atoi(v[i].c_str()), p);
		}
	}
	fin.close();

	std::cout << "step 2" << std::endl;
	p = rootA;
	q = rootB;
	while (p != NULL && p->next!=NULL) {
		if (p->next->data % 2 != 0) {
			p = p->next;
			continue;
		}
		q = insert(p->next, q);
		p->next = p->next->next;

	}

	std::cout << "step 3" << std::endl;
	p = rootA;
	q = rootB->next;
	Node* prev = p;
	while (p != NULL && q != NULL ) {
		Node* tmpp = p->next;
		Node* tmpq = q->next;
		p->next = q;
		q->next = tmpp;
		q = tmpq;
		prev = p;
		p = tmpp;
	}

	if (q != NULL) {
		prev->next->next = q;
	}
	std::cout << "step 4" << std::endl;
	printlist(rootA);
	return 0;
}
