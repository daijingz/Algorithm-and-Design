import java.util.*;

public class BFS {
    //V represents How much vertices we have
    //adj represents the set of edges
    private int V;
    private LinkedList<Integer> adj[];

    //Constructor: build a new BFS object
    BFS(int v) {
        V = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; ++i) {
            adj[i] = new LinkedList();
        }
    }

    //method for adding a new edge into graph
    void addEdge(int v,int w) {
        adj[v].add(w);
    }

    //scanning BFS method for
    void BFS(int s) {
        //Algorithm: we uses a boolean array for all vertices to show whether they are reached
        //If they are reached then true, else false
        boolean visited[] = new boolean[V];

        //Check which vertices are full or not and they are reachable vertices.
        LinkedList<Integer> queue = new LinkedList<Integer>();

        visited[s] = true;
        queue.add(s);

        while (queue.size() != 0) {
            s = queue.poll();
            System.out.print(s + ", ");
            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
}