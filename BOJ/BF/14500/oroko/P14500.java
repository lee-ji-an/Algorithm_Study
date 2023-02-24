import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14500 {

    static int N, M;
    static int[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) map[i][j] = Integer.parseInt(st.nextToken());
        }
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) put(i, j, 0, map[i][j], -1, -1);
        }
        System.out.println(max);
    }

    static int max = 0;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void put(int i, int j, int r, int sum, int pi, int pj) {
        if(r == 3) {
            max = Math.max(max, sum);
            return;
        }

        T(i, j);

        for(int k = 0; k < 4; k++) {
            int ni = i + dr[k];
            int nj = j + dc[k];
            if(0 > ni || ni >= N || 0 > nj || nj >= M) continue;
            if(ni == pi && nj == pj) continue;
            put(ni, nj, r+1, sum + map[ni][nj], i, j);
        }
    }

    public static void T(int i, int j) {
        int sum = map[i][j];
        int cnt = 0;
        int min = Integer.MAX_VALUE;
        for(int k = 0; k < 4; k++) {
            int ni = i + dr[k];
            int nj = j + dc[k];
            if(0 > ni || ni >= N || 0 > nj || nj >= M) continue;
            cnt++;
            sum += map[ni][nj];
            min = Math.min(min, map[ni][nj]);
        }
        if(cnt >= 4) sum -= min;
        max = Math.max(max, sum);
    }
}
