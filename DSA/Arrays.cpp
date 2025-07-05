#include <bits/stdc++.h>
using namespace std;

long long maxSubArraySum(vector<long long> arr)
{
      long long sum = 0, maxSum = LONG_MIN;
      for (int i = 0; i < arr.size(); i++)
      {
            sum += arr[i];
            maxSum = max(maxSum, sum);
            if (sum < 0)
                  sum = 0;
      }
      return sum;
}
int longestSubarrayWithSumK(vector<int> arr, long long k)
{
      int left = 0, right = 0;
      long long sum = 0;
      int maxLen = 0;
      int n = arr.size();
      while (right < n)
      {
            sum += arr[right];
            while (left <= right && sum > k)
            {
                  sum -= arr[left];
                  left++;
            }
            if (sum == k)
            {
                  maxLen = max(maxLen, right - left + 1);
            }
            right++;
      }
      return maxLen;
}
int main()
{
      vector<int> v = {1,
                       2,
                       3,
                       4,
                       5};
      cout << longestSubarrayWithSumK(v, 8);
}