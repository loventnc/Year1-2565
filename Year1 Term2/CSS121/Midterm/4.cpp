#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

typedef pair<int, int> pii;
typedef vector<vector<pii>> graph;
const int INF = numeric_limits<int>::max();

vector<int> dijkstra(const graph& g, int source) {
 int n = g.size();
 vector<int> dist(n, INF);
 dist[source] = 0;
 priority_queue<pii, vector<pii>, greater<pii>> pq;
 pq.push({0, source});
 while (!pq.empty()) {
 int u = pq.top().second;
 int d = pq.top().first;
 pq.pop();
 if (d != dist[u]) continue;
 for (const auto& [v, w] : g[u]) {
 if (dist[u] + w < dist[v]) {
 dist[v] = dist[u] + w;
 pq.push({dist[v], v});
 }
 }
 }
 return dist;
}

int main() {
 int n, m, s;
 cin >> n >> m >> s;
 graph g(n);
 for (int i = 0; i < m; i++) {
 int u, v, w;
 cin >> u >> v >> w;
 g[u].push_back({v, w});
 }
 vector<int> dist = dijkstra(g, s);
 for (int d : dist) {
 if (d == INF) cout << "INF\n";
 else cout << d << '\n';
 }
 return 0;
}