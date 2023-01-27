import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P16948 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r1 = Integer.parseInt(st.nextToken());
        int c1 = Integer.parseInt(st.nextToken());
        int r2 = Integer.parseInt(st.nextToken());
        int c2 = Integer.parseInt(st.nextToken());
        System.out.println(bfs(N, r1, c1, r2, c2));
    }

    static int[] dr = {-2, -2, 0, 0, 2, 2};
    static int[] dc = {-1, 1, -2, 2, -1, 1};
    public static int bfs(int N, int r1, int c1, int r2, int c2) {
        Queue<Pos> q = new LinkedList<>();
        boolean[][] visited = new boolean[N][N];
        q.add(new Pos(r1, c1, 0));
        visited[r1][c1] = true;
        while(!q.isEmpty()) {
            Pos p = q.remove();
            if(p.i == r2 && p.j == c2) return p.cnt;
            for(int k = 0; k < 6; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < N) {
                    if(!visited[ni][nj]) {
                        visited[ni][nj] = true;
                        q.add(new Pos(ni, nj, p.cnt+1));
                    }
                }
            }
        }
        return -1;
    }

    static class Pos {
        int i, j, cnt;
        Pos(int i, int j, int cnt) {
            this.i = i;
            this.j = j;
            this.cnt = cnt;
        }
    }
}
