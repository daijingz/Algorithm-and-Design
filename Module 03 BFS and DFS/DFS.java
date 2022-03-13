import java.util.*;

public class DFS {
    //V represents How much vertices we have
    //adj represents the set of edges
    private int V;
    private LinkedList<Integer> adj[];

    // Constructor for an DFS object
    DFS(int v) {
        V = v;
        adj = new LinkedList[v];
        for (int i=0; i<v; ++i)
            adj[i] = new LinkedList();
    }
    //Add a new edge to the graph
    void addEdge(int v, int w) {
        adj[v].add(w);
    }

    //methods are sub-methods of DFS way
    void DFSUtil(int v,boolean visited[]) {
        visited[v] = true;
        System.out.print(v+", ");
        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n])
                DFSUtil(n, visited);
        }
    }
    // super methods of DFS way
    void DFS(int v) {
        boolean visited[] = new boolean[V];
        DFSUtil(v, visited);
    }
}