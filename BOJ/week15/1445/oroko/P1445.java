import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1445 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        char[][] map = new char[N][M];

        PriorityQueue<Pos> pq = new PriorityQueue<>();
        int[][] dist = new int[N][M];
        for(int i = 0; i < N; i++) {
            String s = br.readLine();
            Arrays.fill(dist[i], Integer.MAX_VALUE);
            for(int j = 0; j < M; j++) {
                map[i][j] = s.charAt(j);
                if(map[i][j] == 'S') {
                    pq.add(new Pos(i, j, 0, 0));
                    dist[i][j] = 0;
                }
            }
        }

        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};
        while(!pq.isEmpty()) {
            Pos p = pq.remove();
            if(map[p.i][p.j] == 'F') {
                System.out.println(p.trash + " " + p.dirty);
                break;
            }
            for(int i = 0; i < 4; i++) {
                int ni = p.i + dr[i];
                int nj = p.j + dc[i];
                if(0 > ni || ni >= N || 0 > nj || nj >= M) continue;
                int nt = p.trash;
                if(map[ni][nj] == 'g') nt++;
                if(dist[ni][nj] > nt) {
                    dist[ni][nj] = nt;
                    int nd = p.dirty;
                    if(map[ni][nj] == '.') {
                        for (int j = 0; j < 4; j++) {
                            int nni = ni + dr[j];
                            int nnj = nj + dc[j];
                            if (0 > nni || nni >= N || 0 > nnj || nnj >= M) continue;
                            if (map[nni][nnj] == 'g') {
                                nd++;
                                break;
                            }
                        }
                    }
                    pq.add(new Pos(ni, nj, nt, nd));
                }
            }
        }
    }

    static class Pos implements Comparable<Pos> {
        int i, j;
        int trash, dirty;

        public Pos(int i, int j, int trash, int dirty) {
            this.i = i;
            this.j = j;
            this.trash = trash;
            this.dirty = dirty;
        }


        @Override
        public int compareTo(Pos o) {
            if(this.trash == o.trash) return Integer.compare(this.dirty, o.dirty);
            return Integer.compare(this.trash, o.trash);
        }
    }
}
