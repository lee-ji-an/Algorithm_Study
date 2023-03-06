import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P7569 {

    static int N, M, H;
    static int[][][] tomato;
    static int raw;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        tomato = new int[H][N][M];
        Queue<Pos> q = new LinkedList<>();
        boolean[][][] visited = new boolean[H][N][M];
        for(int i = 0; i < H; i++) {
            for(int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                for(int k = 0; k < M; k++) {
                    tomato[i][j][k] = Integer.parseInt(st.nextToken());
                    if(tomato[i][j][k] == 1) {
                        q.add(new Pos(i, j, k));
                        visited[i][j][k] = true;
                    } else if(tomato[i][j][k] == 0) raw++;
                }
            }
        }
        System.out.println(raw > 0 ? bfs(q, visited) : 0);
    }

    static int[] dh = {-1, 0, 0, 0, 0, 1};
    static int[] dr = {0, 0, -1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1, 0, 0};
    static int bfs(Queue<Pos> q, boolean[][][] visited) {
        int day = 0;
        while (!q.isEmpty()) {
            day++;

            int len = q.size();
            for(int l = 0; l < len; l++) {
                Pos p = q.remove();
                for(int k = 0; k < 6; k++) {
                    int nh = p.i + dh[k];
                    int nr = p.j + dr[k];
                    int nc = p.k + dc[k];
                    if(0 > nh || nh >= H || 0 > nr || nr >= N || 0 > nc || nc >= M) continue;
                    if(tomato[nh][nr][nc] == 0) {
                        if(visited[nh][nr][nc]) continue;
                        q.add(new Pos(nh, nr, nc));
                        visited[nh][nr][nc] = true;
                    }
                }
            }
            ripe(q);
            if(raw == 0) return day;
        }

        return -1;
    }

    static void ripe(Queue<Pos> q) {
        for(Pos p : q) {
            tomato[p.i][p.j][p.k] = 1;
            raw--;
        }
    }

    static class Pos {
        int i, j, k;

        public Pos(int i, int j, int k) {
            this.i = i;
            this.j = j;
            this.k = k;
        }
    }
}
