import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P17086 {

    static int N, M;
    static boolean[][] shark;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        shark = new boolean[N][M];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) shark[i][j] = st.nextToken().charAt(0) == '1';
        }
        int max = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(!shark[i][j]) max = Math.max(max, bfs(i, j));
            }
        }
        System.out.println(max);
    }

    static int[] dr = {-1, -1, -1, 0, 1, 1, 1, 0};
    static int[] dc = {-1, 0, 1, 1, 1, 0, -1, -1};
    public static int bfs(int si, int sj) {
        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(si, sj, 0));
        boolean[][] visited = new boolean[N][M];
        visited[si][sj] = true;
        while (!q.isEmpty()) {
            Pos p = q.remove();
            for(int k = 0; k < 8; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                    if(!visited[ni][nj]) {
                        if(shark[ni][nj]) return p.cnt + 1;
                        q.add(new Pos(ni, nj, p.cnt + 1));
                        visited[ni][nj] = true;
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
