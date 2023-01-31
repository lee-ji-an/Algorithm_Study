import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P17141 {

    static int N, M;
    static int[][] map;
    static int zero = 0;
    static int min = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        List<Pos> virus = new ArrayList<>();
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] != 1) {
                    if(map[i][j] == 2) virus.add(new Pos(i, j, 0));
                    zero++;
                }
            }
        }
        perm(virus, new boolean[virus.size()], 0, M);
        System.out.println(min == Integer.MAX_VALUE ? -1 : min);
    }

    public static void perm(List<Pos> virus, boolean[] visited, int start, int r) {
        if(r == 0) {
            Queue<Pos> q = new LinkedList<>();
            boolean[][] visited2 = new boolean[N][N];
            for(int i = 0; i < virus.size(); i++) {
                if(visited[i]) {
                    Pos v = virus.get(i);
                    q.add(v);
                    visited2[v.i][v.j] = true;
                }
            }
            int res = bfs(q, visited2);
            if(res >= 0) min = Math.min(min, res);
            return;
        }
        for(int i = start; i < virus.size(); i++) {
            if(!visited[i]) {
                visited[i] = true;
                perm(virus, visited, i+1, r-1);
                visited[i] = false;
            }
        }
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    public static int bfs(Queue<Pos> q, boolean[][] visited) {
        int myzero = zero - M;
        int max = 0;
        while(!q.isEmpty()) {
            Pos p = q.remove();
            max = Math.max(max, p.cnt);
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < N) {
                    if(!visited[ni][nj] && map[ni][nj] != 1) {
                        visited[ni][nj] = true;
                        q.add(new Pos(ni, nj, p.cnt+1));
                        myzero--;
                    }
                }
            }
        }
        return myzero == 0 ? max : -1;
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
