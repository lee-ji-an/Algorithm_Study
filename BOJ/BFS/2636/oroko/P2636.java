import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P2636 {

    static int N, M;
    static boolean[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                if(st.nextToken().charAt(0) == '1') map[i][j] = true;
            }
        }

        bfs();
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    public static void bfs() {
        Queue<Pos> q = new LinkedList<>();
        boolean[][] visited = new boolean[N][M];
        for(int i = 0; i < N; i++) {
            q.add(new Pos(i, 0));
            q.add(new Pos(i, M-1));
            visited[i][0] = visited[i][M-1] = true;
        }
        for(int j = 0; j < M; j++) {
            q.add(new Pos(0, j));
            q.add(new Pos(N-1, j));
            visited[0][j] = visited[N-1][j] = true;
        }

        int time = 0;
        int cnt = 0;
        while(true) {
            Queue<Pos> meltQ = new LinkedList<>();
            while (!q.isEmpty()) {
                Pos p = q.remove();
                for (int k = 0; k < 4; k++) {
                    int ni = p.i + dr[k];
                    int nj = p.j + dc[k];
                    if (0 > ni || ni >= N || 0 > nj || nj >= M) continue;
                    if (visited[ni][nj]) continue;
                    if (!map[ni][nj]) q.add(new Pos(ni, nj));
                    else  meltQ.add(new Pos(ni, nj));
                    visited[ni][nj] = true;
                }
            }

            if(meltQ.isEmpty()) break;
            for (Pos p : meltQ) map[p.i][p.j] = false;
            time++;
            cnt = meltQ.size();
            q = meltQ;
        }

        System.out.println(time);
        System.out.println(cnt);
    }

    static class Pos {
        int i, j;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
