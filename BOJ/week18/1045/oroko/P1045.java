import java.io.*;
import java.util.*;

public class P1045 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<Node>[] list = new List[N];
        for(int i = 0; i < N; i++) list[i] = new ArrayList<>();
        int weight = 1;
        for(int i = 0; i < N; i++) {
            String s = br.readLine();
            for(int j = i+1; j < N; j++) {
                if(s.charAt(j) == 'Y') {
                    list[i].add(new Node(i, j, weight));
                    list[j].add(new Node(j, i, weight++));
                }
            }
        }

        boolean[] visited = new boolean[N];
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.weight, o2.weight));
        pq.add(new Node(-1, 0, 0));
        boolean[][] connected = new boolean[N][N];
        int cnt = 0;
        int[] answer = new int[N];

        while(!pq.isEmpty()) {
            Node v = pq.remove();

            if(visited[v.v2]) continue;
            visited[v.v2] = true;

            if(v.v1 >= 0) {
                connected[v.v1][v.v2] = connected[v.v2][v.v1] = true;
                answer[v.v1]++;
                answer[v.v2]++;
                cnt++;
            }

            for(Node nv : list[v.v2]) {
                if(!visited[nv.v2]) pq.add(nv);
            }
        }

        if(cnt < N-1) {
            System.out.println(-1);
            return;
        }

        if(cnt < M) {
            outer:
            for (int i = 0; i < N; i++) {
                for (Node node : list[i]) {
                    int nv = node.v2;
                    if (connected[i][nv]) continue;
                    answer[i]++;
                    answer[nv]++;
                    cnt++;
                    connected[i][nv] = connected[nv][i] = true;
                    if (cnt == M) break outer;
                }
            }

            if(cnt < M) {
                System.out.println(-1);
                return;
            }
        }

        for(int n : answer) bw.write(n + " ");
        bw.flush();
    }

    static class Node {
        int v1, v2, weight;

        public Node(int v1, int v2, int weight) {
            this.v1 = v1;
            this.v2 = v2;
            this.weight = weight;
        }
    }
}
