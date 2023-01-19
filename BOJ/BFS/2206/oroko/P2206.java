import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P2206 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        boolean[][] map = new boolean[N][M];
        for(int i = 0; i < N; i++) {
            String s = br.readLine();
            for(int j = 0; j < M; j++) map[i][j] = s.charAt(j) == '1';
        }
        System.out.println(bfs(N, M, map));
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static int bfs(int N, int M, boolean[][] map) {

        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(0, 0, 0));
        int[][][] dist = new int[N][M][2];
        dist[0][0][0] = dist[0][0][1] = 1;
        while(!q.isEmpty()) {
            Pos p = q.remove();
            if(p.i == N-1 && p.j == M-1) return p.crash == 0 ? dist[p.i][p.j][0] : dist[p.i][p.j][1];
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                    if(!map[ni][nj] && dist[ni][nj][p.crash] == 0) {  // 벽이 없으면 그냥 통과
                        q.add(new Pos(ni, nj, p.crash));
                        dist[ni][nj][p.crash] = dist[p.i][p.j][p.crash] + 1;
                    }
                    else if(p.crash == 0 && dist[ni][nj][1] == 0) {     // 벽이 있고 부순 적이 없으면 부수고 통과
                        q.add(new Pos(ni, nj, 1));
                        dist[ni][nj][1] = dist[p.i][p.j][0] + 1;
                    }
                }
            }
        }

        return -1;
    }

    static class Pos {
        int i, j;
        int crash;
        public Pos(int i, int j, int crash) {
            this.i = i;
            this.j = j;
            this.crash = crash;
        }
    }
}
