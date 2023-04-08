import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P14950 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        List<Node>[] list = new List[N+1];
        for(int i = 1; i <= N; i++) list[i] = new ArrayList<>();
        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            list[v1].add(new Node(v2, weight));
            list[v2].add(new Node(v1, weight));
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(1, 0));

        boolean[] visited = new boolean[N+1];
        int sum = 0;
        while(!pq.isEmpty()) {
            Node v = pq.remove();
            if(visited[v.v]) continue;
            visited[v.v] = true;
            sum += v.weight;

            for(Node nv : list[v.v]) {
                if(visited[nv.v]) continue;
                pq.add(new Node(nv.v, nv.weight));
            }
        }

        System.out.println((sum + t*(N-1)*(N-2)/2));
    }

    static class Node implements Comparable<Node> {
        int v, weight;

        public Node(int v, int weight) {
            this.v = v;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.weight, o.weight);
        }
    }
}
