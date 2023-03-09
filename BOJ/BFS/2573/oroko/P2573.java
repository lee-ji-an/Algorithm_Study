import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P2573 {

    static int N, M;
    static int[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];

        Queue<Pos> q = new LinkedList<>();
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] > 0) q.add(new Pos(i, j));
            }
        }

        System.out.println(bfs(q));
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static int bfs(Queue<Pos> q) {
        int year = 0;
        while (!q.isEmpty()) {
            if(seperated(q.size(), q.peek())) return year;  // 분리됐으면 반환
            year++;
            int len = q.size();
            Queue<Pos> meltQ = new LinkedList<>();
            for(int l = 0; l < len; l++) {
                Pos p = q.remove();
                int cnt = 0;
                for (int k = 0; k < 4; k++) {
                    int ni = p.i + dr[k];
                    int nj = p.j + dc[k];
                    if (0 > ni || ni >= N || 0 > nj || nj >= M) continue;
                    if (map[ni][nj] == 0) cnt++;
                }
                int weight = map[p.i][p.j] - cnt;
                if(weight > 0) q.add(p);    // 다 안녹았으면 다음 탐색
                if(cnt > 0) meltQ.add(new Pos(p.i, p.j, weight));   // 녹았으면 녹일 목록에 추가
            }
            melt(meltQ);    // 녹이기
        }

        return 0;
    }

    static void melt(Queue<Pos> q) {
        for(Pos p : q) map[p.i][p.j] = p.weight;
    }

    static boolean seperated(int total, Pos start) {
        Queue<Pos> q = new LinkedList<>();
        q.add(start);
        boolean[][] visited = new boolean[N][M];
        visited[start.i][start.j] = true;
        int cnt = 0;
        while(!q.isEmpty()) {
            Pos p = q.remove();
            cnt++;
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if (0 > ni || ni >= N || 0 > nj || nj >= M) continue;
                if(!visited[ni][nj] && map[ni][nj] > 0) {
                    q.add(new Pos(ni, nj));
                    visited[ni][nj] = true;
                }
            }
        }
        return cnt != total;
    }

    static class Pos {
        int i, j, weight;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }

        public Pos(int i, int j, int weight) {
            this.i = i;
            this.j = j;
            this.weight = Math.max(weight, 0);
        }
    }
}
