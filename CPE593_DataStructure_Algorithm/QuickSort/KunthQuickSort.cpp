//CPE593, Assignment 3b, Optional
//
// Author: Yupeng Cao
// ID:     10454637
//https://github.com/CYP0630/Study_Note/tree/master/CPE593_DataStructure_Algorithm/QuickSort

//******************************************************
// Write a golden mean search to find the best k value
// for your \Knuth-optimized partial quicksort.
//******************************************************

// Instruction: Please use C++14 to compile file

#include <iostream>
#include <cmath>
#include <time.h>

using namespace std;

// phi is 1.618.
const double phi = (1+sqrt(5))/2;

//Define a function to generate a random
void RandomArray(int arr[],int n)
{
    int i=0;
    srand( (unsigned)time( NULL ) );
    while(i<n)
    {
        arr[i++]=rand();
    }
}


//Define golden mean search function
//Here refers to reference[1].
int GoldenMeanSearch(int arr[], int n){
    int left = 0, right = n-1;
    int S = (right - left) / phi;
    int x = right - S;
    int y = left + S;

    do{
        if (arr[x] > arr[y]){
            right = y;
            y = x;
            S = (right - left) / phi;
            x = right - S;
        }
        else{
            left = x;
            x = y;
            S = (right - left) / phi;
            y = left + S;
        }
    }
    while (left < right);

    //Return the position of target element
    int point = left;
    return point;
}

// Swap two elements in an array.
void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

// Define Insertion Sort Algorithm
void InsertionSort(int arr[], int n){
    int i, j, key;
    for (i = 1; i < n; i++){
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key){
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = key;
    }
}

//Define Partition Function
//Set pivot and move all smaller (smaller than pivot) to left
//move all greater elements to right
//Here refers to reference[2].
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
void quickSort(int arr[], int left, int right, int k)
{
    int n = sizeof(arr) / sizeof(arr[0]);

    if(left >= right) {
        return ;
    }

    if (left < right)
    {
        int pi = Partition(arr, left, right);
        if (pi - 1 - left > k){
            quickSort(arr, left, pi -1, k);
        }
        if (right - pi > k){
            quickSort(arr, pi+1, right, k);
        }
    }
}

void printArray(int arr[], int n){
    for (int i = 0; i < n; i++)
        cout << arr[i] <<" ";
    cout << endl;
}

// Define Kunth Quick Sort method
void KnuthQuickSort(int arr[], int n){
    int k;
    k = GoldenMeanSearch(arr, n);
    quickSort(arr, 0, n-1, k);
    InsertionSort(arr, n);
    printArray(arr, n);
}

int main() {

    //Calculate Program Running Time
    clock_t start, end;

    //Generate a random array
    //Initial an empty array called arr
    //num is the number of elements in arr
    int num = 10000;
    int arr[num];
    RandomArray(arr, num);
    int n = sizeof(arr) / sizeof(arr[0]);

    start = clock();
    KnuthQuickSort(arr, n);
    end = clock();

    cout << "Running Time" << (double)(end - start)/CLOCKS_PER_SEC <<endl;
    return 0;

}

//Reference:
//[1]. https://stackoverflow.com/questions/44351499/golden-section-search
//[2]. https://www.geeksforgeeks.org/quick-sort/

//More detailed explanation about this homework is here:
//https://github.com/CYP0630/Study_Note/tree/master/CPE593_DataStructure_Algorithm/QuickSort