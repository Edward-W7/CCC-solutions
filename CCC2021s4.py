#include <bits/stdc++.h>
using namespace std;
const int MM = 2e5+5;
typedef pair<int, int> pi;
int N, W, D, dis[MM], idx[MM], a[MM]; vector<int> adj[MM]; set<pi> st; bool vis[MM];
void bfs(int start){
    
    fill(dis, dis+MM, 1e9);   queue<int> q;
    q.push(start); dis[start]=0; vis[start] = true;
    while(!q.empty()) {
        
        int u = q.front(); q.pop();
        for(int v : adj[u]) {
            if(!vis[v]) { q.push(v); dis[v] = dis[u] + 1;  vis[v]=true;}
        }
    }
}

int main(){
    
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> N >> W >> D;
    
    for(int i=1, u, v; i<=W; i++) {
        cin >> u >> v;
        adj[v].push_back(u);
    }
    
    bfs(N);
    for(int i=0; i<N; i++){
        cin >> a[i];   idx[a[i]] = i;
        st.insert({dis[a[i]] + idx[a[i]], a[i]});
    }
    
    for(int i=0, x, y; i<D; i++) {
        cin >> x >> y;  x--; y--;
        st.erase({dis[a[x]] + idx[a[x]], a[x]}); st.erase({dis[a[y]] + idx[a[y]], a[y]});
        swap(idx[a[x]], idx[a[y]]); swap(a[x], a[y]);
        st.insert({dis[a[x]] + idx[a[x]], a[x]}); st.insert({dis[a[y]] + idx[a[y]], a[y]});
        cout << st.begin()->first << "\n";
    }
}
