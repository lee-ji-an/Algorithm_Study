import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P16929 {

    static int N, M;
    static char[][] map;
    static boolean[][] visited;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new char[N][M];
        for(int i = 0; i < N; i++) map[i] = br.readLine().toCharArray();
        visited = new boolean[N][M];
        String answer = "No";
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(!visited[i][j]) {
                    if (dfs(new Pos(i, j, new Pos(-1, -1, null)), 0)) {
                        answer = "Yes";
                        break;
                    }
                }
            }
            if(answer.equals("Yes")) break;
        }
        System.out.println(answer);
    }

    public static boolean dfs(Pos p, int len) {
        if(visited[p.i][p.j] && len >= 4) return true;
        visited[p.i][p.j] = true;
        boolean ret = false;
        for(int k = 0; k < 4; k++) {
            int ni = p.i + dr[k];
            int nj = p.j + dc[k];
            if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                if(map[ni][nj] == map[p.i][p.j] &&
                        (ni != p.prev.i || nj != p.prev.j)) {
                    ret = dfs(new Pos(ni, nj, p), len + 1);
                    if(ret) break;
                }
            }
        }
        return ret;
    }

    static class Pos {
        int i, j;
        Pos prev;
        Pos(int i, int j, Pos prev) {
            this.i = i;
            this.j = j;
            this.prev = prev;
        }
    }
}
