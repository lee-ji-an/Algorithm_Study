import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P13460 {

    static Pos start;
    static int holeI, holeJ;
    static int N, M;
    static boolean[][] map;

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    static class Pos implements Comparable<Pos>, Cloneable {
        int ri, rj, bi, bj, cnt;

        public Pos(int ri, int rj, int bi, int bj, int cnt) {
            this.ri = ri;
            this.rj = rj;
            this.bi = bi;
            this.bj = bj;
            this.cnt = cnt;
        }

        public Pos() {}

        @Override
        public int compareTo(Pos p) {
            return Integer.compare(this.cnt, p.cnt);
        }

        @Override
        public Pos clone() {
            try {
                Pos clone = (Pos) super.clone();
                clone.cnt++;
                // TODO: copy mutable state here, so the clone can't change the internals of the original
                return clone;
            } catch (CloneNotSupportedException e) {
                throw new AssertionError();
            }
        }

        public void move(int i) {
            boolean changeR = false;
            // 빨간구슬 갈 수 있으면 한 칸 이동
            if(ri != holeI || rj != holeJ) {    // 구멍에 빠졌으면 이동 못함
                if (1 <= ri + dr[i] && ri + dr[i] <= N - 2
                        && 1 <= rj + dc[i] && rj + dc[i] <= M - 2) {
                    if (map[ri + dr[i]][rj + dc[i]]) {
                        ri += dr[i];
                        rj += dc[i];
                        changeR = true;
                    }
                }
            }

            // 파란구슬 갈 수 있으면 한 칸 이동
            if(bi != holeI || bj != holeJ) {    // 구멍에 빠졌으면 이동 못함
                if (1 <= bi + dr[i] && bi + dr[i] <= N - 2
                        && 1 <= bj + dc[i] && bj + dc[i] <= M - 2) {
                    if (map[bi + dr[i]][bj + dc[i]]) {
                        bi += dr[i];
                        bj += dc[i];
                    }
                }
            }

            // 두 구슬 겹치는 것 방지 => 하나가 안움직였는데 나머지가 움직여서 겹쳐졌으면 움직인 것 원위치
            if(ri == bi && rj == bj &&
                    (ri != holeI || rj != holeJ)) {
                if(changeR) {
                    ri -= dr[i];
                    rj -= dc[i];
                }
                else {
                    bi -= dr[i];
                    bj -= dc[i];
                }
            }
        }
    }

    public static int bfs() {
        PriorityQueue<Pos> pq = new PriorityQueue<>();  // 시도 횟수 작은 경우부터 탐색
        pq.add(start);
        while(!pq.isEmpty()) {
            Pos p = pq.remove();
            if(p.bi == holeI && p.bj == holeJ) continue;    // 파란구슬이 빠지면 안됨
            if(p.ri == holeI && p.rj == holeJ) return p.cnt;    // 빨간구슬만 빠진 최소 cnt 반환
            if(p.cnt == 10) continue;   // 10회 시도했는데도 안됐으면 안됨
            for(int i = 0; i < 4; i++) {
                Pos np = p.clone();     // 구슬들의 다음 위치
                while(true) {
                    Pos temp = np.clone();
                    np.move(i);
                    if(np.ri == holeI && np.rj == holeJ
                            && np.bi == holeI && np.bj == holeJ) break;     // 둘 다 구멍에 빠졌으면 더 못감
                    if(temp.ri == np.ri && temp.rj == np.rj
                            && temp.bi == np.bi && temp.bj == np.bj) break; // 갈 수 있을만큼 다 갔으면 그만
                }
                if(np.cnt <= 10) pq.add(np);    // 10회 이하로 시도했으면 확인
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new boolean[N][M];    // 갈 수 있는지 없는지로 표시
        start = new Pos();
        for(int i = 0; i < N; i++) {
            String s = br.readLine();
            for(int j = 0; j < M; j++) {
                map[i][j] = true;
                switch (s.charAt(j)) {
                    case '#': map[i][j] = false; break;
                    case 'R': {
                        start.ri = i;
                        start.rj = j;
                        break;
                    }
                    case 'B': {
                        start.bi = i;
                        start.bj = j;
                        break;
                    }
                    case 'O': {
                        holeI = i;
                        holeJ = j;
                        break;
                    }
                    default:
                }
            }
        }
        System.out.println(bfs());
    }
}
