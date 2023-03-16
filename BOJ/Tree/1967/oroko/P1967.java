import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P1967 {

    static int max = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Node[] tree = new Node[N+1];
        for(int i = 1; i <= N; i++) tree[i] = new Node(i);
        for(int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            tree[Integer.parseInt(st.nextToken())].addChild(tree[Integer.parseInt(st.nextToken())], Integer.parseInt(st.nextToken()));
        }
        tree[1].search();
        System.out.println(max);
    }

    static class Node {
        int num;
        int weight;
        List<Node> children;

        public Node(int num) {
            this.num = num;
            this.children = new ArrayList<>();
        }

        public void addChild(Node node, int weight) {
            this.children.add(node);
            node.weight = weight;
        }

        public int search() {
            if(this.children.isEmpty()) return this.weight;

            int first = 0, second = 0;
            for(Node node : this.children) {
                int childWeight = node.search();
                if(childWeight > first) {
                    second = first;
                    first = childWeight;
                } else if(childWeight > second) second = childWeight;
            }

            max = Math.max(max, first + second);
            return this.weight + first;
        }
    }
}
