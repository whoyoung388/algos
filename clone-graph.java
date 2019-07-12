// BFS (this is supppper slow, beats 5%)

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {}

    public Node(int _val,List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        Node root = node;
        Set<Node> nodes = new HashSet<>();
        Queue<Node> queue = new LinkedList<>();
        queue.offer(node);
        while (!queue.isEmpty()) {
            Node n = queue.poll();
            nodes.add(n);
            for (Node neighbor : n.neighbors) {
                if (!nodes.contains(neighbor)) {
                    queue.offer(neighbor);
                }
            }
        }
        
        HashMap<Node, Node> map = new HashMap<>();
        for (Node n : nodes) {
            map.put(n, new Node(n.val, new ArrayList<Node>()));
        }
        
        for (Node n : nodes) {
            Node copyNode = map.get(n);
            for (Node neighbor : n.neighbors) {
                copyNode.neighbors.add(map.get(neighbor));
            }
        }
        
        return map.get(root);
    }
}
