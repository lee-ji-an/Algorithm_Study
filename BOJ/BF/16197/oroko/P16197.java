import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P16197 {

    static int N, M;
    static boolean[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new boolean[N][M];
        Pos[] coins = new Pos[2];
        for(int i = 0; i < N; i++) {
            String s = br.readLine();
            for(int j = 0; j < M; j++) {
                if(s.charAt(j) != '#') map[i][j] = true;
                if(s.charAt(j) == 'o') {
                    if(coins[0] == null) coins[0] = new Pos(i, j);
                    else coins[1] = new Pos(i, j);
                }
            }
        }
        System.out.println(pressButton(coins, 0));
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static int pressButton(Pos[] coins, int cnt) {
        if(cnt >= 10) return -1;

        int min = Integer.MAX_VALUE;
        for(int k = 0; k < 4; k++) {
            int ni1 = coins[0].i + dr[k];
            int nj1 = coins[0].j + dc[k];

            int ni2 = coins[1].i + dr[k];
            int nj2 = coins[1].j + dc[k];

            boolean dropped1 = dropped(ni1, nj1);
            boolean dropped2 = dropped(ni2, nj2);
            if(dropped1 ^ dropped2) return cnt+1;   // 하나 떨어졌으면 끝
            if(!dropped1) continue;     // 둘 다 떨어졌으면 다음 버튼 누르기 탐색

            // 둘 다 남아있으면 다음 탐색
            Pos[] nCoins = new Pos[2];
            nCoins[0] = map[ni1][nj1] ? new Pos(ni1, nj1) : coins[0];
            nCoins[1] = map[ni2][nj2] ? new Pos(ni2, nj2) : coins[1];

            int res = pressButton(nCoins, cnt+1);
            if(res > 0) min = Math.min(min, res);
        }

        return min == Integer.MAX_VALUE ? -1 : min;
    }

    static boolean dropped(int i, int j) {
        if(0 > i || i >= N) return false;
        if(0 > j || j >= M) return false;
        return true;
    }

    static class Pos {
        int i, j;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
