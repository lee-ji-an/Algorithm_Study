import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N;
    static Pos shark;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                int n = Integer.parseInt(st.nextToken());
                map[i][j] = n;
                if (n == 9) {
                    shark = new Pos(i, j, 2, 0);
                    map[i][j] = 0;
                }
            }
        }
        int time = 0;
        int eat = 0;
        while (true) {
            int gap = bfs();
            if(gap < 0) break;
            eat++;
            if(eat == shark.size) {
                shark.size++;
                eat = 0;
            }
            time += gap;
        }
        System.out.println(time);
    }

    static int[] dr = {-1, 0, 0, 1};
    static int[] dc = {0, -1, 1, 0};
    static int bfs() {
        PriorityQueue<Pos> q = new PriorityQueue<>();
        q.add(shark);
        boolean[][] visited = new boolean[N][N];
        visited[shark.i][shark.j] = true;
        while (!q.isEmpty()) {
            Pos p = q.remove();
            if(map[p.i][p.j] > 0 && map[p.i][p.j] < shark.size) {
                shark.i = p.i;
                shark.j = p.j;
                map[p.i][p.j] = 0;
                return p.cnt;
            }
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < N) {
                    if(!visited[ni][nj] && map[ni][nj] <= shark.size) {
                        q.add(new Pos(ni, nj, map[ni][nj], p.cnt+1));
                        visited[ni][nj] = true;
                    }
                }
            }
        }
        return -1;
    }

    static class Pos implements Comparable<Pos> {
        int i, j;
        int size;
        int cnt;

        public Pos(int i, int j, int size, int cnt) {
            this.i = i;
            this.j = j;
            this.size = size;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Pos o) {
            if(this.cnt == o.cnt) {
                if(this.i == o.i) return Integer.compare(this.j, o.j);
                return Integer.compare(this.i, o.i);
            }
            return Integer.compare(this.cnt, o.cnt);
        }
    }
}
