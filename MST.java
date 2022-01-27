// Jingze Dai, 400201059, daij24
import java.util.*;
import java.lang.*;

class MST {
    private static class Edge implements Comparable<Edge> {
        int src, dest, weight;
        public int compareTo(Edge target) {
            return this.weight - target.weight;
        }
    }

    private static class subset {
        int parent, rank;
    }

    private int V;
    private Edge[] edges;

    private MST(int vertex, int edge) {
        try {
            V = vertex;
            edges = new Edge[edge];
            for (int i = 0; i < edge; ++i) {
                edges[i] = new Edge();
            }
        } catch (IllegalArgumentException e){
            System.out.println("Wrong input vertex or edge values");
            System.out.println("Reminder: V is positive integer");
            System.out.println("Reminder: E is positive integer");
        }
    }

    private int find(subset[] subsets, int i) {
        if (subsets[i].parent != i) {
            subsets[i].parent = find(subsets, subsets[i].parent);
        }
        return subsets[i].parent;
    }

    private void Union(subset[] sbtt, int index1, int index2) {
        int root1 = find(sbtt, index1);
        int root2 = find(sbtt, index2);

        if (sbtt[root1].rank < sbtt[root2].rank) {
            sbtt[root1].parent = root2;
        } else if (sbtt[root1].rank > sbtt[root2].rank) {
            sbtt[root2].parent = root1;
        } else {
            sbtt[root2].parent = root1;
            sbtt[root1].rank = sbtt[root1].rank + 1;
        }
    }

    private void Kruskal() {
        Edge[] result = new Edge[V];
        int amount_edge = 0;

        int i = 0;
        while (i < V) {
            result[i] = new Edge();
            ++i;
        }
        Arrays.sort(edges);

        subset[] sbtt = new subset[V];
        i = 0;
        while (i < V) {
            sbtt[i] = new subset();
            sbtt[i].parent = i;
            sbtt[i].rank = 0;
            ++i;
        }

        i = 0;
        while (amount_edge < V - 1) {
            Edge next_edge = edges[i++];
            int x = find(sbtt, next_edge.src);
            int y = find(sbtt, next_edge.dest);

            if (x != y) {
                result[amount_edge++] = next_edge;
                Union(sbtt, x, y);
            }
        }

        System.out.println("MST edges: ");
        System.out.println();
        int minimumCost = 0;
        for (i = 0; i < amount_edge; ++i) {
            System.out.println("Edge " + result[i].src + " - " + result[i].dest);
            System.out.println("Edge Cost: " + result[i].weight);
            System.out.println();
            minimumCost += result[i].weight;
        }
        System.out.println("Total MST Cost: " + minimumCost);
    }

    public static void main(String[] args) {
        MST Graph1 = new MST(5, 6);

        Graph1.edges[0].src = 0;
        Graph1.edges[0].dest = 1;
        Graph1.edges[0].weight = 4;

        Graph1.edges[1].src = 0;
        Graph1.edges[1].dest = 2;
        Graph1.edges[1].weight = 7;

        Graph1.edges[2].src = 0;
        Graph1.edges[2].dest = 3;
        Graph1.edges[2].weight = 15;

        Graph1.edges[3].src = 1;
        Graph1.edges[3].dest = 3;
        Graph1.edges[3].weight = 5;

        Graph1.edges[4].src = 2;
        Graph1.edges[4].dest = 3;
        Graph1.edges[4].weight = 8;

        Graph1.edges[5].src = 1;
        Graph1.edges[5].dest = 4;
        Graph1.edges[5].weight = 6;

        Graph1.Kruskal();
    }
}