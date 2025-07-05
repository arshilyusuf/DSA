#include <bits/stdc++.h>
using namespace std;
// Merge Sort:
// Time Complexity: O(n log n) (best, average, worst case)
// Space Complexity: O(n) (for auxiliary space during merge)
// Stability: Stable (maintains the relative order of equal elements)
// When to Use:
//   - Use when stable sorting is required.
//   - Use when worst-case performance (O(n log n)) is needed, e.g., sorting linked lists or large datasets.
//   - Suitable for external sorting (large data that doesn’t fit in memory).

// Quick Sort:
// Time Complexity: O(n log n) (average case), O(n^2) (worst case)
// Space Complexity: O(log n) (for recursive calls), O(n) in worst case due to recursion stack
// Stability: Not stable
// When to Use:
//   - Use for in-place sorting when you need fast average-case performance.
//   - Typically faster than merge sort in practice (despite the O(n^2) worst case).
//   - Not suitable when stability is important.

// Bubble Sort:
// Time Complexity: O(n^2) (best, average, worst case)
// Space Complexity: O(1) (in-place sorting)
// Stability: Stable
// When to Use:
//   - Only suitable for small datasets due to its inefficiency.
//   - Use if the data is nearly sorted (best case: O(n)).

// Selection Sort:
// Time Complexity: O(n^2) (best, average, worst case)
// Space Complexity: O(1) (in-place sorting)
// Stability: Not stable
// When to Use:
//   - Use when you have very small datasets or when memory usage is a concern.
//   - Its primary advantage is its space efficiency, but it is inefficient on large datasets.

// Insertion Sort:
// Time Complexity: O(n^2) (average, worst case), O(n) (best case when the array is already sorted)
// Space Complexity: O(1) (in-place sorting)
// Stability: Stable
// When to Use:
//   - Use when the data is nearly sorted or for small datasets.
//   - It is efficient for small datasets and when only a few elements are out of place.

// Heap Sort:
// Time Complexity: O(n log n) (best, average, worst case)
// Space Complexity: O(1) (in-place sorting)
// Stability: Not stable
// When to Use:
//   - Use when you need an in-place sorting algorithm with guaranteed O(n log n) performance.
//   - Suitable for large datasets and situations where memory usage is a concern.
//   - Not as fast as quick sort in practice, but it is stable in terms of time complexity.

// Counting Sort:
// Time Complexity: O(n + k) (where k is the range of the input)
// Space Complexity: O(n + k) (for the counting array and the output array)
// Stability: Stable
// When to Use:
//   - Use when the range of elements (k) is small and known in advance.
//   - Best suited for integers or categorical data where counting occurrences is easy.
//   - Can be used for sorting large data when the range of elements is constrained.

// Radix Sort:
// Time Complexity: O(nk) (where k is the number of digits in the largest number)
// Space Complexity: O(n + k) (for the output array and counting arrays)
// Stability: Stable
// When to Use:
//   - Use when you need to sort integers or strings with a fixed number of digits/characters.
//   - Efficient for sorting large datasets with small ranges (e.g., sorting phone numbers, social security numbers).

// Bucket Sort:
// Time Complexity: O(n + k) (best case when elements are uniformly distributed, k is the number of buckets)
// Space Complexity: O(n + k) (for the buckets and the output array)
// Stability: Stable (if stable sorting is used within buckets)
// When to Use:
//   - Use when data is uniformly distributed and when the range of elements is known.
//   - Best used when the input data is spread out evenly (e.g., sorting floating-point numbers in the range [0, 1]).

// Cycle Sort:
// Time Complexity: O(n^2) (best, average, worst case)
// Space Complexity: O(1) (in-place sorting)
// Stability: Not stable
// When to Use:
//   - Use when minimizing the number of writes is important (e.g., memory write is costly).
//   - Best for situations where the input has a known range and the number of swaps needs to be minimized.

void merge(vector<int> &arr, int low, int mid, int high)
{
      vector<int> temp;
      int left = low;
      int right = mid + 1;
      while (left <= mid && right <= high)
      {
            if (arr[left] <= arr[right])
            {
                  temp.push_back(arr[left]);
                  left++;
            }
            else
            {
                  temp.push_back(arr[right]);
                  right++;
            }
      }
      while (left <= mid)
      {
            temp.push_back(arr[left]);
            left++;
      }
      while (right <= high)
      {
            temp.push_back(arr[right]);
            right++;
      }
      for (int i = low; i <= high; i++)
      {
            arr[i] = temp[i - low];
      }
}
void mergeSort(vector<int> &arr, int low, int high)
{
      // TC:
      // best, avg, worst = O(nlogn)
      // SC: O(n)

      if (low >= high)
            return;
      int mid = (low + high) / 2;
      mergeSort(arr, low, mid);
      mergeSort(arr, mid + 1, high);
      merge(arr, low, mid, high);
}
int partitionArray(vector<int> &arr, int low, int high)
{
      int pivot = arr[low];
      int i = low;
      int j = high;
      while (i < j)
      {
            while (arr[i] <= pivot && i <= high - 1)
                  i++;
            while (arr[j] > pivot && j >= low + 1)
                  j--;
            if (i < j)
                  swap(arr[i], arr[j]);
      }
      swap(arr[low], arr[j]);
      return j;
}
void quickSort(vector<int> &arr, int low, int high)
{
    
      if (low < high)
      {
            int pIndex = partitionArray(arr, low, high);
            quickSort(arr, low, pIndex - 1);
            quickSort(arr, pIndex + 1, high);
      }
}
void cycleSort(vector<int> &arr)
{
      int n = arr.size();

      // Traverse the array to place elements in correct position
      for (int cycleStart = 0; cycleStart < n - 1; cycleStart++)
      {
            int item = arr[cycleStart];

            // Find the number of elements smaller than the current element
            int position = cycleStart;
            for (int i = cycleStart + 1; i < n; i++)
            {
                  if (arr[i] < item)
                  {
                        position++;
                  }
            }

            // If the item is already in the correct position, skip it
            if (position == cycleStart)
            {
                  continue;
            }

            // Otherwise, put the element to the correct position
            while (item == arr[position])
            {
                  position++;
            }
            swap(arr[position], item);

            // Rotate the rest of the cycle
            while (position != cycleStart)
            {
                  position = cycleStart;
                  for (int i = cycleStart + 1; i < n; i++)
                  {
                        if (arr[i] < item)
                        {
                              position++;
                        }
                  }

                  while (item == arr[position])
                  {
                        position++;
                  }
                  swap(arr[position], item);
            }
      }
}
void maxHeapify(vector<int> &arr, int i, int n)
{
      int left = 2 * i + 1; // 0 based indexing
      int right = 2 * i + 2;
      int largest = i;

      if (left < n && arr[left] > arr[largest])
      {
            largest = left;
      }
      if (right < n && arr[right] > arr[largest])
      {
            largest = right;
      }
      if (largest != i)
      {
            swap(arr[i], arr[largest]);
            maxHeapify(arr, largest, n);
      }
}

void heapSort(vector<int>&arr){
      int n = arr.size();

      // Step 1: Build max heap
      for (int i = n / 2 - 1; i >= 0; i--)
      {
            maxHeapify(arr, i, n);
      }

      // Step 2: Extract elements one by one from the heap
      for (int i = n - 1; i > 0; i--)
      {
            swap(arr[0], arr[i]);  // Move max to end
            maxHeapify(arr, 0, i); // Heapify the reduced heap
      }
}
int main()
{
      vector<int> arr = {5, 2, 8, 1,
                         9, 3, 7, 6, 4};
      int n = arr.size();
      // quickSort(arr, 0, n - 1);
      heapSort(arr);
      for (int i = 0; i < n; i++)
            cout << arr[i] << " ";
}