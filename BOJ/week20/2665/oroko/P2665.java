import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

public class P2665 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        boolean[][] map = new boolean[N][N];
        for(int i = 0; i < N; i++) {
            String s = br.readLine();
            for(int j = 0; j < N; j++) map[i][j] = s.charAt(j) == '1';
        }

        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.weight, o2.weight));
        int[][] change = new int[N][N];
        for(int i = 0; i < N; i++) Arrays.fill(change[i], Integer.MAX_VALUE);
        pq.add(new Node(0, 0, 0));

        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};

        while(!pq.isEmpty()) {
            Node p = pq.remove();

            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 > ni || ni >= N || 0 > nj || nj >= N) continue;
                int weight = p.weight + (map[ni][nj] ? 0 : 1);
                if(change[ni][nj] > weight) {
                    change[ni][nj] = weight;
                    pq.add(new Node(ni, nj, weight));
                }
            }
        }

        System.out.println(change[N-1][N-1]);
    }

    static class Node {
        int i, j;
        int weight;

        public Node(int i, int j, int weight) {
            this.i = i;
            this.j = j;
            this.weight = weight;
        }
    }
}
