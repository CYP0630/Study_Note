//CPE593, Assignment 4, QuickSort
//
// Author: Yupeng Cao
// ID:     10454637
//

// The implementation of QuickSort
//
// Instruction: Please use C++11 to compile file in terminal
//              g++ main.cpp
//              ./a.out "hw2a.dat"


#include <iostream>
#include <stdio.h>
#include <time.h>


using namespace std;

//Define swap function
//Change the position for two elements in array
void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

//Define Partition Function
//Set pivot and move all smaller (smaller than pivot) to left
//move all greater elements to right
//Here refers to reference[1].
int Partition (int arr[], int left, int right)
{
    //Define pivot variable
    int pivot;
    pivot = (arr[right]);

    int i;
    i = left - 1;
    int j = left;

    for (j; j <= right - 1; j++)
    {
        if(arr[j]<pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[right]);
    return (i + 1);
}

//Define quickSort Function
//arr[] is input array
//left is the smallest index value
//right is the largest index value
void quickSort(int arr[], int left, int right)
{
    if(left >= right) {
        return ;
    }

    if (left < right)
    {
        int pi = Partition(arr, left, right);
        quickSort(arr, left, pi -1);
        quickSort(arr, pi+1, right );
    }
}

//Main Function
int main(int argc, char *argv[]) {

    clock_t start, end;

    int arr_0[] = {2, 4, 8, 16, 32, 20, 10, 5, 1};
    int m = sizeof(arr_0) / sizeof(arr_0[0]);

    start = clock();
    quickSort(arr_0, 0, m - 1);
    end = clock();


    int h;
    for (h=0; h<m; h++)
    {
        cout <<arr_0[h]<<" ";
    }
    cout<<"\n";
    cout << "Running Time" << (double)(end - start)/CLOCKS_PER_SEC <<endl;
    return 0;
}

//Reference:
//[1]. https://www.geeksforgeeks.org/quick-sort/
//[2]. http://www.voidcn.com/article/p-xhncrhby-kw.html

//Comment:
//I can finished QuickSort function and I can read the ".dat" file from terminal.
//But I faced some bugs, when I trying to operate for each line from .dat file
//I will continue to solve these problems.

