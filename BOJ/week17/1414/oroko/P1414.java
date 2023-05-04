import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class P1414 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        List<Node>[] g = new List[N];
        for(int i = 0; i < N; i++) g[i] = new ArrayList<>();

        int totalLen = 0;
        for(int i = 0; i < N; i++) {
            String s = br.readLine();
            for(int j = 0; j < N; j++) {
                char c = s.charAt(j);
                if(c == '0') continue;
                Node node = new Node(j, c);
                g[i].add(node);
                totalLen += node.weight;

                g[j].add(new Node(i, c));
            }
        }

        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.weight, o2.weight));
        pq.add(new Node(0, 0));
        boolean[] visited = new boolean[N];
        int cnt = 0;
        int sum = 0;
        while(!pq.isEmpty()) {
            Node n = pq.remove();
            if(visited[n.v]) continue;
            visited[n.v] = true;
            sum += n.weight;
            cnt++;

            for(Node nn : g[n.v]) {
                if(visited[nn.v]) continue;
                pq.add(nn);
            }
        }

        if(cnt < N) System.out.println(-1);
        else System.out.println(totalLen - sum);
    }

    static class Node {
        int v, weight;

        public Node(int v, char weight) {
            this(v, Character.isLowerCase(weight) ? weight-'a'+1 : weight-'A'+27);
        }

        public Node(int v, int weight) {
            this.v = v;
            this.weight = weight;
        }
    }
}
