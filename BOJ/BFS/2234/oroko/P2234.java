import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P2234 {

    static int N, M;
    static int[][] map;
    static int[][] area;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        area = new int[N][M];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) map[i][j] = Integer.parseInt(st.nextToken());
        }
        int cnt = 0;
        int max = 0;
        boolean[][] visited = new boolean[N][M];
        List<Integer> size = new ArrayList<>();
        int id = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(!visited[i][j]) {
                    size.add(bfs(i, j, visited, id));
                    max = Math.max(max, size.get(id++));
                    cnt++;
                }
            }
        }

        System.out.println(cnt);
        System.out.println(max);
        System.out.println(maxSum(size));
    }

    static int[] dr = {0, -1, 0, 1};
    static int[] dc = {-1, 0, 1, 0};
    public static int bfs(int si, int sj, boolean[][] visited, int id) {
        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(si, sj));
        visited[si][sj] = true;
        area[si][sj] = id;
        int cnt = 0;
        while (!q.isEmpty()) {
            Pos p = q.remove();
            cnt++;
            for(int k = 0; k < 4; k++) {
                if((map[p.i][p.j] & (1 << k)) == 0) {
                    int ni = p.i + dr[k];
                    int nj = p.j + dc[k];
                    if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                        if (!visited[ni][nj]) {
                            visited[ni][nj] = true;
                            q.add(new Pos(ni, nj));
                            area[ni][nj] = id;
                        }
                    }
                }
            }
        }
        return cnt;
    }

    public static int maxSum(List<Integer> size) {
        int maxsum = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                for(int k = 0; k < 4; k++) {
                    int ni = i + dr[k];
                    int nj = j + dc[k];
                    if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                        if(area[ni][nj] != area[i][j])
                            maxsum = Math.max(maxsum, size.get(area[ni][nj]) + size.get(area[i][j]));
                    }
                }
            }
        }
        return maxsum;
    }

    static class Pos {
        int i, j;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
