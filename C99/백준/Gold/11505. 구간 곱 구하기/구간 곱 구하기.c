#include <stdio.h>
#define MOD 1000000007

long long arr[1000001] = {0};
long long tree[4000004] = {0};

long long init(int start, int end, int node) {
    if (start == end) {
        return tree[node] = arr[start];
    }
    int mid = (start + end) / 2;
    return tree[node] = (init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1)) % MOD;
}

long long update(int start, int end, int node, int index, long long value) {
    if (index < start || index > end) {
        return tree[node];
    }
    if (start == end) {
        return tree[node] = value;
    }
    int mid = (start + end) / 2;
    return tree[node] = (update(start, mid, node * 2, index, value) * update(mid + 1, end, node * 2 + 1, index, value)) % MOD;
}

long long query(int start, int end, int node, int left, int right) {
    if (left > end || right < start) {
        return 1;
    }
    if (left <= start && end <= right) {
        return tree[node];
    }
    int mid = (start + end) / 2;
    return (query(start, mid, node * 2, left, right) * query(mid + 1, end, node * 2 + 1, left, right)) % MOD;
}

int main() {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    for (int i = 1; i <= n; i++) {
        scanf("%lld", &arr[i]);
    }
    init(1, n, 1);
    for (int i = 0; i < m + k; i++) {
        int a, b;
        long long c;
        scanf("%d %d %lld", &a, &b, &c);
        if (a == 1) {
            update(1, n, 1, b, c);
        } else if (a == 2) {
            printf("%lld\n", query(1, n, 1, b, c));
        }
    }
    return 0;
}