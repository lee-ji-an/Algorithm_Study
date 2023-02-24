package baekjoon.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P17822 {

    static int N, M;
    static int[][] plates;
    static int sum = 0, cnt = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());

        plates = new int[N+1][M];
        for(int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                plates[i][j] = Integer.parseInt(st.nextToken());
                increase(i, j);
            }
        }

        for(int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            rotate(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );

            boolean erase = false;
            for(int i = 1; i <= N; i++) {
                for(int j = 0; j < M; j++) {
                    if(plates[i][j] > 0) erase |= erase(i, j);
                }
            }
            if(!erase) arrange();
        }

        System.out.println(sum());
    }

    static void rotate(int x, int d, int k) {
        if(d == 0) k = M-k;
        for(int i = x; i <= N; i += x) {
            Queue<Integer> q = new LinkedList<>();
            int idx = k;
            for(int j = 0; j < M; j++, idx++) q.add(plates[i][idx%M]);
            for(int j = 0; j < M; j++) plates[i][j] = q.remove();
        }
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static boolean erase(int si, int sj) {
        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(si, sj));
        int target = plates[si][sj];
        decrease(si, sj);
        plates[si][sj] = 0;
        boolean erase = false;

        while (!q.isEmpty()) {
            Pos p = q.remove();
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = (p.j + dc[k] + M) % M;
                if(0 >= ni || ni > N) continue;
                if(plates[ni][nj] == target) {
                    decrease(ni, nj);
                    plates[ni][nj] = 0;
                    q.add(new Pos(ni, nj));
                    erase = true;
                }
            }
        }
        if(!erase) {
            plates[si][sj] = target;
            increase(si, sj);
        }
        return erase;
    }

    static void arrange() {
        double avg = (double) sum / cnt;
        sum = 0;
        cnt = 0;
        for(int i = 1; i <= N; i++) {
            for(int j = 0; j < M; j++) {
                if(plates[i][j] == 0) continue;

                if(plates[i][j] > avg) plates[i][j]--;
                else if(plates[i][j] < avg) plates[i][j]++;

                if(plates[i][j] > 0) {
                    increase(i, j);
                }
            }
        }
    }

    static int sum() {
        int sum = 0;
        for(int i = 1; i <= N; i++) {
            for(int j = 0; j < M; j++) sum += plates[i][j];
        }
        return sum;
    }

    static void increase(int i, int j) {
        sum += plates[i][j];
        cnt++;
    }

    static void decrease(int i, int j) {
        sum -= plates[i][j];
        cnt--;
    }

    static class Pos {
        int i, j;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}