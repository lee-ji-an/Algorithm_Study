import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P1600 {

    static int K;
    static int N, M;
    static boolean[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        map = new boolean[N][M];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) map[i][j] = st.nextToken().charAt(0) == '1';
        }
        System.out.println(bfs());
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static int[] hdr = {1, 2, 2, 1, -1, -2, -2, -1};
    static int[] hdc = {-2, -1, 1, 2, 2, 1, -1, -2};
    public static int bfs() {
        Queue<Pos> q = new LinkedList<>();
        int[][][] dist = new int[N][M][K+1];
        q.add(new Pos(0, 0, 0));
        Arrays.fill(dist[0][0], 1);
        while(!q.isEmpty()) {
            Pos p = q.remove();
            if(p.i == N-1 && p.j == M-1) return dist[p.i][p.j][p.horse] - 1;
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                    if(dist[ni][nj][p.horse] == 0 && !map[ni][nj]) {
                        dist[ni][nj][p.horse] = dist[p.i][p.j][p.horse] + 1;
                        q.add(new Pos(ni, nj, p.horse));
                    }
                }
            }
            if(p.horse < K) {
                for(int k = 0; k < 8; k++) {
                    int ni = p.i + hdr[k];
                    int nj = p.j + hdc[k];
                    if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                        if(dist[ni][nj][p.horse+1] == 0) {
                            dist[ni][nj][p.horse+1] = dist[p.i][p.j][p.horse] + 1;
                            q.add(new Pos(ni, nj, p.horse+1));
                        }
                    }
                }
            }
        }
        return -1;
    }

    static class Pos {
        int i, j, horse;
        Pos(int i, int j, int horse) {
            this.i = i;
            this.j = j;
            this.horse = horse;
        }
    }
}
