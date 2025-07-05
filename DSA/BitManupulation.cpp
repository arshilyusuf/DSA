#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <numeric>
#include <array>
using namespace std;

string toBinary(int n)
{
    string ans = "";
    while (n)
    {
        if ((n & 1) == 1)
            ans += '1';
        else
            ans += '0';
        n /= 2;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

int toDecimal(string s)
{
    int j = s.size() - 1;
    int power = 1;
    int ans = 0;

    while (j >= 0)
    {
        if (s[j] == '1')
            ans += power;
        j--;
        power *= 2;
    }

    return ans;
}

bool checkIthBit(int n, int bit)
{
    return ((n & (1 << bit)) != 0);
}
bool checkIthBitUsingRightShift(int n, int bit)
{
    return ((n >> bit) & 1) == 1;
}
void setIthBit(int &n, int bit)
{
    n = n | (1 << bit);
}
void unsetIthBit(int &n, int bit)
{
    n = n & (~(1 << bit));
}
void toggleIthBit(int &n, int bit)
{
    n = n ^ (1 << bit);
}
void removeLastSetBit(int &n)
{
    n = n & (n - 1);
}
bool ifPowerOf2(int n)
{
    return (n & (n - 1)) == 0;
}
int countSetBits(int n)
{
    int counter = 0;
    while (n)
    {
        counter += (n & 1);
        n = n >> 1;
    }
    return counter;
}
int SecondCountSetBits(int n)
{
    int counter = 0;
    while (n)
    {
        n = n & (n - 1);
        counter++;
    }
    return counter;
}
int grayCode(int i)
{
    return i ^ (i >> 1);
}
void swap(int &a, int &b)
{
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
}
int main()
{
    cout << toDecimal("1101") << endl;
    int x = 3, y = 8;
    swap(x, y);
    cout << x << " " << y << endl;
    ;
    cout << checkIthBit(13, 1) << endl;
    cout << checkIthBitUsingRightShift(13, 1) << endl;
    int a = 9;
    setIthBit(a, 2);
    cout << a << endl;
    unsetIthBit(a, 2);
    cout << a << endl;
    toggleIthBit(a, 2);
    cout << a << endl;
    removeLastSetBit(a);
    cout << a << endl;
    cout << ifPowerOf2(8) << endl;
    cout << countSetBits(15) << endl;
    cout << SecondCountSetBits(15) << endl;
    cout << grayCode(7) << endl;

    return 0;
}