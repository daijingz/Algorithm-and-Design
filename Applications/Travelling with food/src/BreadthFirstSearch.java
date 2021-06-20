//Jingze Dai, 400201059, daij24
//Date: 01/04/2020
import java.util.*;

public class BreadthFirstSearch {
    //V represents How much vertices we have
    //adj represents the set of edges
	private int V;
    private LinkedList<Integer> adj[];

    //Constructor: build a new BFS object
    BreadthFirstSearch(int v) {
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
    //test cases
    public static void main(String args[]) {
        BreadthFirstSearch g = new BreadthFirstSearch(33);
        //Input all edges
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        g.addEdge(3, 4);
        g.addEdge(4, 5);
        g.addEdge(5, 6);
        g.addEdge(6, 7);
        g.addEdge(2, 8);
        g.addEdge(5, 8);
        g.addEdge(8, 9);
        g.addEdge(9, 10);
        g.addEdge(10, 11);
        g.addEdge(11, 12);
        g.addEdge(12, 13);
        g.addEdge(12, 14);
        g.addEdge(14, 15);
        g.addEdge(15, 16);
        g.addEdge(16, 17);
        g.addEdge(17, 18);
        g.addEdge(17, 7);
        g.addEdge(7, 19);
        g.addEdge(19, 32);
        g.addEdge(17, 19);
        g.addEdge(20, 18);
        g.addEdge(11, 20);
        g.addEdge(20, 9);
        g.addEdge(9, 21);
        g.addEdge(21, 22);
        g.addEdge(13, 23);
        g.addEdge(23, 24);
        g.addEdge(24, 25);
        g.addEdge(25, 26);
        g.addEdge(26, 27);
        g.addEdge(27, 28);
        g.addEdge(28, 22);
        g.addEdge(25, 29);
        g.addEdge(24, 29);
        g.addEdge(29, 30);
        g.addEdge(30, 13);
        g.addEdge(30, 15);
        g.addEdge(15, 31);
        g.addEdge(14, 30);
        g.addEdge(7, 20);
        g.addEdge(12, 22);
        g.addEdge(28, 23);
        g.addEdge(24, 30);
        g.addEdge(24, 13);
        g.addEdge(18, 7);
        g.addEdge(14, 18);
        g.addEdge(14, 11);
        g.addEdge(11, 18);
        g.addEdge(21, 11);
        g.addEdge(16, 31);

        System.out.print("BFS: ");
        g.BFS(1);
    }
}
