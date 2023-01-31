import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P4991 {

    static int N, M;
    static char[][] map;
    static int min;
    static int[][] dist;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            if(M == 0 && N == 0) break;
            map = new char[N][M];
            Map<Integer, Pos> target = new HashMap<>();
            int dirtyId = 1;
            for(int i = 0; i < N; i++) {
                map[i] = br.readLine().toCharArray();
                for(int j = 0; j < M; j++) {
                    if(map[i][j] == 'o') target.put(0, new Pos(i, j, 0));
                    else if(map[i][j] == '*') target.put(dirtyId++, new Pos(i, j, 0));
                }
            }
            dist = new int[dirtyId][dirtyId];
            for(int i = 0; i < dirtyId; i++) {
                for(int j = i+1; j < dirtyId; j++) {
                    dist[i][j] = dist[j][i] = bfs(target.get(i), target.get(j));
                }
            }
            min = Integer.MAX_VALUE;
            perm(new int[dirtyId-1], dirtyId-1, 0, new boolean[dirtyId]);
            System.out.println(min);
        }
    }

    public static void perm(int[] sub, int n, int r, boolean[] visited) {
        if(r == n) {
            int sum = dist[0][sub[0]];
            for(int i = 1; i < n; i++) {
                if(dist[sub[i-1]][sub[i]] == -1) {
                    sum = -1;
                    break;
                }
                sum += dist[sub[i-1]][sub[i]];
            }
            min = Math.min(min, sum);
            return;
        }
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                visited[i] = true;
                sub[r] = i+1;
                perm(sub, n, r+1, visited);
                visited[i] = false;
            }
        }
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    public static int bfs(Pos src, Pos dest) {
        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(src.i, src.j, 0));
        boolean[][] visited = new boolean[N][M];
        while (!q.isEmpty()) {
            Pos p = q.remove();
            if(p.i == dest.i && p.j == dest.j) return p.cnt;
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                    if(!visited[ni][nj] && map[ni][nj] != 'x') {
                        visited[ni][nj] = true;
                        q.add(new Pos(ni, nj, p.cnt + 1));
                    }
                }
            }
        }
        return -1;
    }

    static class Pos {
        int i, j, cnt;

        public Pos(int i, int j, int cnt) {
            this.i = i;
            this.j = j;
            this.cnt = cnt;
        }
    }
}
