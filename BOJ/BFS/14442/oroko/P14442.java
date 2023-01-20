import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P14442 {
    static int N, M, K;
    static boolean[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        map = new boolean[N][M];
        for(int i = 0; i < N; i++) {
            String s = br.readLine();
            for(int j = 0; j < M; j++) map[i][j] = s.charAt(j) == '1';
        }
        System.out.println(bfs());
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    public static int bfs() {
        Queue<Pos> q = new LinkedList<>();
        boolean[][][] visited = new boolean[N][M][K+1];
        Arrays.fill(visited[0][0], true);
        q.add(new Pos(0, 0, 0, 1));
        while (!q.isEmpty()) {
            Pos p = q.remove();
            if(p.i == N-1 && p.j == M-1) return p.cnt;
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                    if(!map[ni][nj] && !visited[ni][nj][p.crash]) {
                        q.add(new Pos(ni, nj, p.crash, p.cnt+1));
                        visited[ni][nj][p.crash] = true;
                    } else if(p.crash < K && !visited[ni][nj][p.crash+1]) {
                        q.add(new Pos(ni, nj, p.crash + 1, p.cnt+1));
                        visited[ni][nj][p.crash+1] = true;
                    }
                }
            }
        }
        return -1;
    }

    static class Pos {
        int i, j, crash, cnt;
        Pos(int i, int j, int crash, int cnt) {
            this.i = i;
            this.j = j;
            this.crash = crash;
            this.cnt = cnt;
        }
    }
}
