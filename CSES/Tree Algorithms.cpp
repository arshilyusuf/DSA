#include <bits/stdc++.h>
using namespace std;
using ll = long long;
//Subtree Queries
const int MAXN = 200000 + 5;

vector<int> adj[MAXN];
int st[MAXN], en[MAXN];
int timer = 0;
ll val[MAXN];

void dfs(int u, int p) {
    st[u] = timer++;
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
    }
    en[u] = timer - 1;
}

class NumArray {
    int n;
    vector<ll> nums;      // flattened base array
    vector<ll> seg;       // segment tree

    ll build(int idx, int l, int r) {
        if (l == r) {
            seg[idx] = nums[l];
            return seg[idx];
        }
        int mid = (l + r) / 2;
        ll left = build(2 * idx + 1, l, mid);
        ll right = build(2 * idx + 2, mid + 1, r);
        seg[idx] = left + right;
        return seg[idx];
    }

    void updateHelper(int idx, int sl, int sr, int pos, ll diff) {
        if (pos < sl || pos > sr) return;
        seg[idx] += diff;
        if (sl != sr) {
            int mid = (sl + sr) / 2;
            updateHelper(2 * idx + 1, sl, mid, pos, diff);
            updateHelper(2 * idx + 2, mid + 1, sr, pos, diff);
        }
    }

    ll queryHelper(int idx, int sl, int sr, int l, int r) {
        if (l <= sl && sr <= r) return seg[idx];
        if (sr < l || sl > r) return 0;
        int mid = (sl + sr) / 2;
        return queryHelper(2 * idx + 1, sl, mid, l, r) +
               queryHelper(2 * idx + 2, mid + 1, sr, l, r);
    }

public:
    NumArray(const vector<ll>& input) {
        n = input.size();
        nums = input;
        seg.assign(4 * n, 0);
        if (n > 0)
            build(0, 0, n - 1);
    }

    void update(int index, ll val) {
        if (index < 0 || index >= n) return;
        ll diff = val - nums[index];
        nums[index] = val;
        updateHelper(0, 0, n - 1, index, diff);
    }

    ll sumRange(int left, int right) {
        if (left < 0) left = 0;
        if (right >= n) right = n - 1;
        if (left > right) return 0;
        return queryHelper(0, 0, n - 1, left, right);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        cin >> val[i];
    }

    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    vector<ll> flat(n);
    for (int i = 1; i <= n; i++) {
        flat[st[i]] = val[i];
    }

    NumArray segTree(flat);

    while (q--) {
        int t, s;
        cin >> t >> s;
        if (t == 1) {
            ll x;
            cin >> x;
            segTree.update(st[s], x);
        } else if (t == 2) {
            cout << segTree.sumRange(st[s], en[s]) << '\n';
        }
    }

    return 0;
}