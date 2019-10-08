#include <iostream>

using namespace std;

void naive_search(char *str, char *pat){

    // strlen: return the length of char
    int M = strlen(pat);
    int N = strlen(str);

    for(int i=0; i <= N - M; i++){
        int j = 0;

        for(j=0; j < M; j++)
            if (str[i+j] != pat[j])
                break;
        if (j == M)
            cout << "Pattern found at position" << i <<endl;
    }
}

int main() {
    char str[] = "AABBCAABCABCA";
    char pat[] = "BCA";

    naive_search(str, pat);
    return 0;
}