import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P6087 {

    static int N, M;
    static char[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        map = new char[N][M];
        int si = 0, sj = 0;
        for(int i = 0; i < N; i++) {
            map[i] = br.readLine().toCharArray();
            for(int j = 0; j < M; j++) {
                if(map[i][j] == 'C') {
                    si = i;
                    sj = j;
                    break;
                }
            }
        }
        System.out.println(bfs(si, sj));
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static int bfs(int si, int sj) {
        PriorityQueue<Pos> q = new PriorityQueue<>();
        q.add(new Pos(si, sj, 0, -1));
        map[si][sj] = '.';
        int[][][] mirror = new int[N][M][4];
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(i != si || j != sj) Arrays.fill(mirror[i][j], -1);
            }
        }

        while(!q.isEmpty()) {
            Pos p = q.remove();
            if(map[p.i][p.j] == 'C') return p.mirror;
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj & nj < M) {
                    if(map[ni][nj] != '*') {
                        int nMirror = p.mirror + addMirror(p.dir, k);
                        if(mirror[ni][nj][k] == -1 || nMirror < mirror[ni][nj][k]) {
                            q.add(new Pos(ni, nj, p.mirror + addMirror(p.dir, k), k));
                            mirror[ni][nj][k] = nMirror;
                        }
                    }
                }
            }
        }
        return -1;
    }

    public static int addMirror(int dir1, int dir2) {
        if(dir1 == -1) return 0;
        return dir1 % 2 == dir2 % 2 ? 0 : 1;
    }

    static class Pos implements Comparable<Pos>{
        int i, j;
        int mirror;
        int dir;

        @Override
        public int compareTo(Pos o) {
            return Integer.compare(this.mirror, o.mirror);
        }

        Pos(int i, int j, int mirror, int dir) {
            this.i = i;
            this.j = j;
            this.dir = dir;
            this.mirror = mirror;
        }
    }

}
