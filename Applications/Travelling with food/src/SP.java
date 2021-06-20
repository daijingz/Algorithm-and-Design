import java.util.*; 
public class SP {
    // dist represents value of edge
    private int dist[]; 
    private Set<Integer> settled; 
    private PriorityQueue<Node> pq; 
    private int V; // Number of vertices
    // connection of vertices.
    List<List<Node> > adj; 

    //Constructor of Shortest path objects
    public SP(int V) {
        this.V = V; 
        dist = new int[V]; 
        settled = new HashSet<Integer>(); 
        pq = new PriorityQueue<Node>(V, new Node()); 
    } 
  
    //Function for Dijkstra's Algorithm: start at cty 0
    public void dijkstra(List<List<Node> > adj, int src) {
        this.adj = adj; 

        // give initial value of distance: Max value
        // for all vertices the source cannot arrive directly assume the distance is infinite.
        for (int i = 0; i < V; i++) 
            dist[i] = Integer.MAX_VALUE; 
  
        // Add city 0 to the priority queue
        pq.add(new Node(src, 0)); 
  
        // Distance to the source (city 0) is 0
        dist[src] = 0; 
        while (settled.size() != V) {
            int u = pq.remove().node;
            //renewing number of smallest value
            settled.add(u); 
            e_Neighbours(u); 
        } 
    } 
  
    // Function to process all the neighbours of marked and marked over and over again
    private void e_Neighbours(int u) {
        int edgeDistance = -1; 
        int newDistance = -1; 

        for (int i = 0; i < adj.get(u).size(); i++) { 
            Node v = adj.get(u).get(i);
            if (!settled.contains(v.node)) { 
                edgeDistance = v.cost; 
                newDistance = dist[u] + edgeDistance; 
  
                // If new distance is cheaper in edge
                if (newDistance < dist[v.node]) {
                    dist[v.node] = newDistance;
                }
                pq.add(new Node(v.node, dist[v.node])); 
            } 
        } 
    } 
  
    // Driver code 
    public static void main(String arg[]) {
        // Size 32
        // source: city 0(boston)
        int V = 32; 
        int source = 0; 

        // connected edges 
        List<List<Node> > adj = new ArrayList<List<Node> >(); 
  
        // Initialize list for all nodes
        for (int i = 0; i < V; i++) { 
            List<Node> item = new ArrayList<Node>(); 
            adj.add(item); 
        } 
  
        // Inputs for graph (all edges)
        adj.get(0).add(new Node(1, 4)); 
  
        adj.get(1).add(new Node(2, 5)); 
        adj.get(1).add(new Node(7, 5)); 
        
        adj.get(2).add(new Node(3, 4)); 
        
        adj.get(3).add(new Node(4, 5)); 
  
        adj.get(4).add(new Node(5, 4)); 
        adj.get(4).add(new Node(7, 4));
        
        adj.get(5).add(new Node(6, 5));
        
        adj.get(6).add(new Node(18, 4)); 
        adj.get(6).add(new Node(19, 4));
        
        adj.get(7).add(new Node(8, 5));
        
        adj.get(8).add(new Node(9, 4)); 
        adj.get(8).add(new Node(20, 4));
        
        adj.get(9).add(new Node(10, 5));
        
        adj.get(10).add(new Node(11, 4)); 
        adj.get(10).add(new Node(19, 4));
        adj.get(10).add(new Node(17, 4));
        
        adj.get(11).add(new Node(12, 5)); 
        adj.get(11).add(new Node(13, 5));
        adj.get(11).add(new Node(21, 5));
        
        adj.get(12).add(new Node(22, 4));
        
        adj.get(13).add(new Node(14, 5)); 
        adj.get(13).add(new Node(29, 5));
        adj.get(13).add(new Node(17, 5));
        adj.get(13).add(new Node(10, 5));
        
        adj.get(14).add(new Node(15, 4)); 
        adj.get(14).add(new Node(30, 4));
        
        adj.get(15).add(new Node(16, 5)); 
        adj.get(15).add(new Node(30, 5));
        
        adj.get(16).add(new Node(17, 4)); 
        adj.get(16).add(new Node(6, 4));
        adj.get(16).add(new Node(18, 4));
        
        adj.get(17).add(new Node(6, 5));
        
        adj.get(18).add(new Node(31, 4));
        
        adj.get(19).add(new Node(17, 5)); 
        adj.get(19).add(new Node(8, 5));
        
        adj.get(20).add(new Node(21, 4)); 
        adj.get(20).add(new Node(10, 4));
        
        adj.get(22).add(new Node(23, 5));
        
        adj.get(23).add(new Node(24, 4)); 
        adj.get(23).add(new Node(28, 4));
        adj.get(23).add(new Node(29, 4)); 
        adj.get(23).add(new Node(14, 4));
        
        adj.get(24).add(new Node(25, 5)); 
        adj.get(24).add(new Node(28, 5));
        
        adj.get(25).add(new Node(26, 4));
        
        adj.get(26).add(new Node(27, 5));
        
        adj.get(27).add(new Node(21, 4)); 
        adj.get(27).add(new Node(22, 4));
        
        adj.get(28).add(new Node(29, 5));
        
        adj.get(29).add(new Node(12, 4)); 
        adj.get(29).add(new Node(14, 4));
        // Calculate the single source shortest path 
        SP dpq = new SP(V); 
        dpq.dijkstra(adj, source); 
  
        // Print the shortest path to city 21(Minneapolis)
        System.out.print("The shorted path from node :");
        System.out.println(source + " to " + 21 + " is "
                + dpq.dist[21]);
    } 
} 
  
// Class to represent a node in the graph 
class Node implements Comparator<Node> {
    //node number
    //cost in the city restaurant
    public int node; 
    public int cost; 
  
    public Node() { }

    //constructor of Node object
    public Node(int node, int cost) {
        this.node = node; 
        this.cost = cost; 
    } 
    //Check which cost is larger
    @Override
    public int compare(Node node1, Node node2) {
        if (node1.cost < node2.cost) 
            return -1; 
        if (node1.cost > node2.cost) 
            return 1; 
        return 0; 
    } 
} 
